from create_connection import con, c

db_connect = con
cursor = con.cursor()
def create_table(db_connect , tablename, **args):
    str = ""
    for key, value in args.items():
        str = str+" "+key+" "+value+","
    print(str)
    #con.execute(f"""CREATE TABLE {tablename}({str})""")
    db_connect.execute(f"""CREATE TABLE School(name TEXT, address TEXT, contact TEXT)""")
    db_connect.commit()

#create_table(data_connect)

def insert_data_into_db(db_connect, table, data):
    db_connect.execute(f"""INSERT INTO {table} VALUES('convent', 'pune', '3456')""")
    db_connect.commit()

#insert_data_into_db(db_connect, 'School' ,'data')

def get_data_from_table(cursor, table):
    cursor.execute(f"""SELECT * FROM {table}""")
    print(cursor.fetchall())


get_data_from_table(cursor, 'School')


def insert_mutiple_data_into_db(db_connect, table, *data):
    for value in data:
        db_connect.execute(f"""INSERT INTO {table} VALUES("{value[0]}", "{value[1]}", "{value[2]}")""")
        db_connect.commit()

input_data = [
    ['vidya', 'mumbai', '456786'],
    ['vidya3', 'bang', '456776'],
    ['vidya5', 'gwalior', '456787'],
    ['vidya6', 'Nagpur', '456781']
]
#insert_mutiple_data_into_db(db_connect, 'School', input_data)