import sqlite3
import os
from datetime import datetime

DB_PATH = "logs/testforge.db"

def setup_database():
    """Create the database and table if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp       TEXT,
            function_name   TEXT,
            accepted        INTEGER,
            was_edited      INTEGER,
            reject_reason   TEXT,
            prompt_version  TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_session(function_name, accepted, was_edited=False, reason=""):
    """Save one review result to the database"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """INSERT INTO sessions
           (timestamp, function_name, accepted, was_edited, reject_reason, prompt_version)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (datetime.now().isoformat(), function_name,
         int(accepted), int(was_edited), reason, "v1.0")
    )
    conn.commit()
    conn.close()
    print(f"  Logged: {function_name} → {'ACCEPTED' if accepted else 'REJECTED'}")