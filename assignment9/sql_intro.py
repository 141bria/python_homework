import _sqlite3
with _sqlite3.connect() as conn:
    cursor = conn.cursor()