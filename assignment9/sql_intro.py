import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers(
        publisher_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER PRIMARY KEY
        ) 
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines(
        magazine_name TEXT NOT NULL UNIQUE,
        magazine_id INTEGER PRIMARY KEY,
        publisher_id INTERGER
        ) 
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscibers(
        subscriber_name TEXT NOT NULL UNIQUE,
        subscriber_address TEXT NOT NULL UNIQUE,
        subscriber_id INTEGER,
        magazine_id INTEGER
            ) 
            """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions(
        expirate_date TEXT NOT NULL
        ) 
    """)
except sqlite3.Error as e:
            print(e)
def add_publisher(cursor,publisher_name,publisher_id):
    try:
        cursor.execute("INSERT INTO Publishers (publisher_name,publisher_id)) VALUES (?,?)",(publisher_name, publisher_id))
    except sqlite3.IntegrityError:
          print(f"{publisher_name} is already in the datatbase.")

def add_magazines(cursor,magazine_name,magazine_id,publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (magazine_name,magazine_id,publisher_id) VALUES (?,?,?)",(magazine_name,magazine_id,publisher_id))
    except sqlite3.IntegrityError:
          print(f"{magazine_name} is already in the datatbase.")

def add_subscriber(cursor,subscriber_name,subscriber_address,subscriber_id,magazine_id):
    try:
        cursor.execute("INSERT INTO Subscribers (subscriber_name,subscriber_address,subscriber_id,magazine_id) VALUES (?,?,?,?)",(subscriber_name,subscriber_address,subscriber_id,magazine_id))
    except sqlite3.IntegrityError:
          print(f"{subscriber_name} is already in the datatbase.")