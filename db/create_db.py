import sqlite3
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

DB_PATH = config["db_path"]

def create_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Existing DB dropped: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # --- EXAMPLE TABLE — edit/replace as needed ---
    c.execute("""
        CREATE TABLE IF NOT EXISTS file_list (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name   TEXT NOT NULL UNIQUE,
            file_path   TEXT NOT NULL,
            codec       TEXT NOT NULL,
            bitrate     TEXT NOT NULL,
            file_size   TEXT NOT NULL,
            film_length TEXT NOT NULL,
            film_type   TEXT NOT NULL,
            created_at  TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- ADD MORE TABLES HERE ---

    conn.commit()
    conn.close()
    print(f"DB created: {DB_PATH}")

if __name__ == "__main__":
    create_db()
