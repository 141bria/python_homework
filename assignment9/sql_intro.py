import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
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