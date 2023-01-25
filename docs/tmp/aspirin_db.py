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

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_table = """ CREATE TABLE IF NOT EXISTS plans (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        code text NOT NULL,
                                        name text,
                                        email text,
                                        n integer,
                                        turnover integer,
                                        kved text
                                    ); """


def create_plan(conn, plan):
    sql = ''' INSERT INTO plans(code, name, email, n, turnover, kved)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, plan)
    conn.commit()
    return cur.lastrowid


def select_all_plans(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM plans")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_plan_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM plans WHERE id=?", (id,))
    rows = cur.fetchall()

    for row in rows:
        print(row)


database = r"c:/work/python/aspirin/aspirinsqlite.db"

conn = create_connection(database)

