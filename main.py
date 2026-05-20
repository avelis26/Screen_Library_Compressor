from fs.scan_fs import scan
from db.write_to_db import insert_file_list

if __name__ == "__main__":
    print("Scanning movies...")
    movies = scan("movies")
    print(f"Found: {len(movies)} files")

    print("Writing to DB...")
    insert_file_list(movies)

    print("Scanning shows...")
    shows = scan("shows")
    print(f"Found: {len(shows)} files")

    print("Writing to DB...")
    insert_file_list(shows)
