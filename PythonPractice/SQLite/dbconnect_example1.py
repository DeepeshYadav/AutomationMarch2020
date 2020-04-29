import sqlite3

con = sqlite3.connect('employee.db')
c = con.cursor()
#c.execute("""CREATE TABLE employee(
#            first text,
#            last text,
#            pay integer)""")


c.execute("""INSERT INTO employee VALUES('Rahul2', 'Sharma2', 50000)""")
con.commit()

c.execute("""Select * from employee""")
print(c.fetchall())

c.execute(("""Select * from employee where last='Sharma1'"""))
print(c.fetchall())

con.close()