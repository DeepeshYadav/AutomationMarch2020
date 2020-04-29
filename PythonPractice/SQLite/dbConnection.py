import sqlite3

con = sqlite3.connect("student.db")

#con.execute("""CREATE TABLE employee("
            # Name text,
            # rollno integer,
            # mobile integer ")""")


#con.commit()
con.execute("""INSERT INTO employee VALUES("rahul", 2345, 23445)""")

con.commit()


