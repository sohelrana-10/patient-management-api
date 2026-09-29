import sqlite3

DATABASE_NAME = "patient_management.db"


def get_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)
