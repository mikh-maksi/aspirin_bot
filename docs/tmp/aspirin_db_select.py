import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM plans")
    rows = cur.fetchall()

    for row in rows:
        print(row)

database = r"c:/work/python/aspirin/aspirinsqlite.db"

conn = create_connection(database)

select_all_tasks(conn)