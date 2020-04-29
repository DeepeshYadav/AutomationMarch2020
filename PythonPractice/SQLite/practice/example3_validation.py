import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
user_data = [['rahul', 'convent', 'Pune'],
             ['jitendra', 'public', 'Indore'],
             ['manoj', 'private', 'bhopal'],
             ['rahul', 'convent', 'Mumbai']]

dbtable = 'student'


def create_table(table, name, school, address):
    query = """CREATE TABLE {}({} TEXT, {} TEXT, {} TEXT)""".format(table, name, school, address)
    print(query)
    cur.execute(query)
    con.commit()


def insert_data(table, input_data):
    for data in input_data:
        select_query = "SELECT * FROM {} where name='{}'".format(table, data[0])
        print(select_query)
        cur.execute(select_query)
        if cur.fetchall():
            print("This name is already exist :", data[0])
            continue
        else:
            insert_query = "INSERT INTO {} VALUES(?, ?, ?)".format(table)
            cur.execute(insert_query,(data[0], data[1], data[2]))
            con.commit()

def get_data_from_table(table):
    select_query = "SELECT * FROM {}".format(table)
    cur.execute(select_query)
    return cur.fetchall()




create_table(dbtable, 'name', 'school', 'address')
insert_data(dbtable, user_data)
print(get_data_from_table(dbtable))

