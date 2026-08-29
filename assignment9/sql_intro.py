import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
except sqlite3.Error as e:
    print(e)