import os
import json
import subprocess
import argparse

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)


def probe_file(path):
    """Run ffprobe on a file. Returns (codec, bitrate_mbps, duration_mins) or None if not a video."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=codec_name,bit_rate,duration",
        "-of", "json",
        path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(result.stdout)
        streams = data.get("streams", [])
        if not streams:
            return None

        s = streams[0]
        codec = s.get("codec_name")

        # bit_rate may be missing at stream level; fall back to format level
        bitrate = s.get("bit_rate")
        if not bitrate:
            fmt_cmd = [
                "ffprobe", "-v", "error",
                "-show_entries", "format=bit_rate,duration",
                "-of", "json",
                path
            ]
            fmt_result = subprocess.run(fmt_cmd, capture_output=True, text=True, timeout=30)
            fmt_data = json.loads(fmt_result.stdout).get("format", {})
            bitrate = fmt_data.get("bit_rate")
            duration = s.get("duration") or fmt_data.get("duration")
        else:
            duration = s.get("duration")

        if not codec or not bitrate or not duration:
            return None

        bitrate_mbps = f"{int(bitrate) / 1_000_000:.1f}Mbps"
        duration_mins = f"{float(duration) / 60:.1f}m"

        return codec, bitrate_mbps, duration_mins

    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception):
        return None


def scan(mode):
    if mode == "movies":
        scan_path = config["movies_path"]
    elif mode == "shows":
        scan_path = config["shows_path"]
    else:
        raise ValueError(f"Invalid mode: {mode}")

    exts = {e.lower() for e in config["file_exts"]}
    min_bytes = config["min_file_size"]

    results = []

    for root, _, files in os.walk(scan_path):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in exts:
                continue

            if ("-trailer." in fname) == True:
                continue

            fpath = os.path.join(root, fname)
            fsize_bytes = os.path.getsize(fpath)

            if fsize_bytes < min_bytes:
                continue

            probe = probe_file(fpath)
            if probe is None:
                continue

            codec, bitrate, film_length = probe
            file_size = f"{fsize_bytes / 1_000_000:.0f}Mb"

            results.append({
                "file_path":   fpath,
                "codec":       codec,
                "bitrate":     bitrate,
                "file_size":   file_size,
                "film_length": film_length,
            })

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["movies", "shows"])
    args = parser.parse_args()

    rows = scan(args.mode)
    for r in rows:
        print(r)