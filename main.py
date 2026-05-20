from fs.scan_fs import scan
from db.write_to_db import insert_file_list

if __name__ == "__main__":
    print("Scanning movies...")
    rows = scan("movies")
    print(f"Found: {len(rows)} files")

    print("Writing to DB...")
    insert_file_list(rows)
