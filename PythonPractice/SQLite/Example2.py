import sqlite3

con = sqlite3.connect("car.db")
c = con.cursor()

# Create table in th DB
# con.execute("""CREATE TABLE cars(
#             Name TEXT)""")

# Insert values int the DB
#con.execute("""INSERT INTO cars VALUES('Honda')""")
list = ['Mahindra', 'XUV', 'Indigo', 'TATA']

for car in list:
    con.execute(f"""INSERT INTO cars VALUES('{car}')""")
    con.commit()

# Get data from the DB
#c.execute("""SELECT * FROM cars""")

c.execute("""SELECT * FROM cars where name='Honda'""")
data = c.fetchall()

for value in data:
    print(type(value))
    print(value)


#con.commit()