from aspirin_db import create_connection, create_table, create_plan, select_all_plans, select_plan_by_id


database = r"c:/work/python/aspirin/aspirinsqlite.db"

conn = create_connection(database)

select_all_plans(conn)


plan = ('code1', 'name', 'email',0,1000,'82.29')
# project_id = create_plan(conn, plan)