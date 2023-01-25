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

def create_plan(conn, plan):
    sql = ''' INSERT INTO plans(code, name, email, n, turnover, kved)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, plan)
    conn.commit()
    return cur.lastrowid


database = r"c:/work/python/aspirin/aspirinsqlite.db"

conn = create_connection(database)

plan = ('code', 'name', 'email',0,1000,'82.29');
project_id = create_plan(conn, plan)


# if __name__ == '__main__':
#     create_connection(r"c:/work/python/aspirin/aspirinsqlite.db")