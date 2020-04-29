import sqlite3

con = sqlite3.connect('itpd.db')
c = con.cursor()

con.execute("""CREATE TABLE student(
            name TEXT,
            roll INTEGER)""")


con.execute("""INSERT INTO student VALUES('Harish', 234)""")
con.commit()

con.execute("""SELECT * FROM student""")
print(c.fetchall())