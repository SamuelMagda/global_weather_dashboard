"""
SQLite database utility for Global Weather Dashboard.
Handles connection creation and ensures schema consistency.
"""

import sqlite3
from config import DB_PATH


def get_conn():
    """Return a SQLite connection and ensure 'weather' table exists."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            ts TEXT,
            city TEXT,
            country TEXT,
            temp REAL,
            feels_like REAL,
            humidity REAL,
            wind REAL,
            sunrise TEXT,
            sunset TEXT
        )
    """)
    return conn
