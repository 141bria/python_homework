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
        CREATE TABLE IF NOT EXISTS Subscribers(
        subscriber_name TEXT NOT NULL UNIQUE,
        subscriber_address TEXT NOT NULL UNIQUE,
        subscriber_id INTEGER,
        magazine_id INTEGER
            ) 
            """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions(
        expiration_date TEXT NOT NULL
        ) 
    """)
        def add_publisher(cursor,publisher_name,publisher_id):
            try:
                cursor.execute("INSERT INTO Publishers (publisher_name,publisher_id) VALUES (?,?)",(publisher_name, publisher_id))
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
        def add_subscriptions(cursor,expiration_date):
            try:
                cursor.execute("INSERT INTO Subscriptions (expiration_date) VALUES(?)",(expiration_date,))
            except sqlite3.Integrity.Error:
                print(f"{expiration_date} is already in the database")
        add_publisher(cursor,"Jasmine",3)
        add_publisher(cursor,"Ashton",2)
        add_publisher(cursor,"Brianna",1)
        add_magazines(cursor,"Vogue",271,3)
        add_magazines(cursor,"Times",364,2)
        add_magazines(cursor,"Juvia's Place",652,1)
        add_subscriber(cursor,"Jake","1212 Boston Ave, Jacksonville, Florida,32202",20,271)
        add_subscriber(cursor,"Christopher","1919 Forest Hill Drive, Charlotte, North Carolina,28202",4,364)
        add_subscriber(cursor,"Jolene","1717 Popolar Avenue, Memphis,Tennessee,38134",5,652)
        add_subscriptions(cursor,"August 19,2027")
        add_subscriptions(cursor,"December 30,2029")
        add_subscriptions(cursor,"April 2,2031")
        conn.commit()
except sqlite3.IntegrityError as e:
    print(e)

##to add data call functions!!! thats why its not in the tables
cursor.execute("SELECT * FROM Subscribers;")
Subscribers = cursor.fetchall()
for row in Subscribers:
    print(row)

cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name;")
Magazines = cursor.fetchall()
for row in Magazines:
    print(row)

cursor.execute("SELECT Magazines.magazine_name,Publishers.publisher_name FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.publisher_name= 'Jasmine'; ")
publisher_magazines = cursor.fetchall()
for row in publisher_magazines:
    print(row)