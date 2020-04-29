import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
dbtable = "bike"

# CREATE TABLE
createquery =  """CREATE TABLE {} (Modal TEXT, Company TEXT, REgiNo INTEGER)""".format(dbtable)
print(createquery)
con.execute(createquery)
con.commit()


# "INSERT INTO TABLE VALUES(?, ? ?)", (value1, value2, value3)
INSERT_QUERY = "INSERT INTO {} VALUES(?, ?, ?)".format(dbtable)
con.execute(INSERT_QUERY, ('Apache', 'TVS', 3452))
con.commit()

# INSERT INTO TABLE VALUES(:key1, :key2, :key3), {'key1':value1, 'key2':value2, key3':value3}
INSERT_QUERY_NEW = "INSERT INTO {} VALUES(:modal, :company, :regino)".format(dbtable)
con.execute(INSERT_QUERY_NEW, {'modal': 'Scooty', 'company': 'TVS', 'regino':3456})
con.commit()

# SELECT QUERY TO GET THE DATA
SELECT_QUERY = "SELECT * FROM {}".format(dbtable)
cur.execute(SELECT_QUERY)
data = cur.fetchall()
print(data)

con.close()