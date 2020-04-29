import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.execute("CREATE TABLE school(name TEXT, address TEXT, rank INTEGER)")
con.commit()

cur.execute("INSERT INTO school VALUES(?, ?, ?)", ('SIMBY', 'PUNE', 1))
con.commit()

cur.execute("SELECT * FROM school where name=?", ('SIMBY',)),

print(cur.fetchall())
