import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
except sqlite3.Error as e:
    print(e)
cursor.execute("""""
CREATE TABLE IF NOT EXSISTS Publishers(
) 
""")
cursor.execute("""""
CREATE TABLE IF NOT EXSISTS Magazines(
) 
""")
cursor.execute("""""
CREATE TABLE IF NOT EXSISTS Subscibers(
) 
""")
cursor.execute("""""
CREATE TABLE IF NOT EXSISTS Subscriptions(
) 
""")