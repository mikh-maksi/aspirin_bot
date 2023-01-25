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

database = r"c:/work/python/aspirin/aspirinsqlite.db"

conn = create_connection(database)

if conn is not None:
    create_table(conn, sql_create_table)
else:
    print("Error! cannot create the database connection.")


# if __name__ == '__main__':
#     create_connection(r"c:/work/python/aspirin/aspirinsqlite.db")