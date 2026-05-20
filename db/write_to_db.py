import sqlite3
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

DB_PATH = config["db_path"]

def insert_file_list(rows):
    """Insert scan results into file_list table. Skips duplicates by file_path."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    inserted = 0
    skipped = 0

    for row in rows:
        try:
            c.execute("""
                INSERT INTO file_list (file_name, file_path, codec, bitrate_Mbps, file_size_Mb, film_length_m, film_type)
                VALUES (:file_name, :file_path, :codec, :bitrate_Mbps, :file_size_Mb, :film_length_m, :film_type)
            """, row)
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1

    conn.commit()
    conn.close()

    print(f"Inserted: {inserted} | Skipped (duplicate): {skipped}")