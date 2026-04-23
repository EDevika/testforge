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

def show_report():
    """Read the SQLite database and print an acceptance rate report"""
    conn = sqlite3.connect(DB_PATH)

    rows = conn.execute("""
        SELECT function_name, accepted, was_edited, reject_reason, timestamp
        FROM sessions
        ORDER BY timestamp DESC
    """).fetchall()

    conn.close()

    if not rows:
        print("\n  No sessions logged yet. Run TestForge first!")
        return

    # Calculate stats
    total    = len(rows)
    accepted = sum(1 for r in rows if r[1] == 1)
    rejected = sum(1 for r in rows if r[1] == 0)
    edited   = sum(1 for r in rows if r[2] == 1)
    rate     = (accepted / total) * 100

    # Print report
    print("\n" + "="*60)
    print("  TESTFORGE — ACCEPTANCE RATE REPORT")
    print("="*60)
    print(f"  Total tests generated  : {total}")
    print(f"  Accepted               : {accepted} ✅")
    print(f"  Rejected               : {rejected} ❌")
    print(f"  Edited before accept   : {edited} ✏️")
    print(f"  Acceptance rate        : {rate:.1f}%")
    print("="*60)

    if rate == 100:
        print("  Prompt quality: EXCELLENT 🏆 — AI nailed every test!")
    elif rate >= 80:
        print("  Prompt quality: GOOD 👍 — Minor improvements needed")
    elif rate >= 60:
        print("  Prompt quality: AVERAGE ⚠️  — Refine your prompts")
    else:
        print("  Prompt quality: POOR 🔴 — Prompts need major work")

    print("="*60)
    print("\n  Recent sessions:")
    print(f"  {'Function':<25} {'Result':<10} {'Edited':<8} {'Time'}")
    print("  " + "-"*60)

    for row in rows[:10]:
        function_name = row[0]
        result        = "ACCEPTED" if row[1] else "REJECTED"
        was_edited    = "Yes" if row[2] else "No"
        timestamp     = row[4][:19].replace("T", " ")
        print(f"  {function_name:<25} {result:<10} {was_edited:<8} {timestamp}")

    print("\n" + "="*60 + "\n")