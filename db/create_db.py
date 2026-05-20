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
        CREATE TABLE IF NOT EXISTS example_table (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            text_col    TEXT NOT NULL,
            int_col     INTEGER,
            real_col    REAL,
            bool_col    INTEGER DEFAULT 0,       -- SQLite has no BOOL; use 0/1
            created_at  TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- ADD MORE TABLES HERE ---

    conn.commit()
    conn.close()
    print(f"DB created: {DB_PATH}")

if __name__ == "__main__":
    create_db()