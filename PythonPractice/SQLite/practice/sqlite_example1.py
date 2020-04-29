import sqlite3

con = sqlite3.connect('student.db')
cur = con.cursor()

table_name = "student_info"
student_detail = [['stu1', 345, 7658943534],
                  ['stu2', 445, 9658943534],
                  ['stu3', 545, 8658943534]
                  ]

student_detail2 = [['stu4', 645, 8858943534]]

#con.execute("""CREATE TABLE student_info(Name TEXT, rollno INTEGER, mobile INTEGER)""")
#con.commit()

#con.execute("INSERT INTO "+table_name+" VALUES('Rahul', 3456, 7507456238)")
#con.commit()

# for data in student_detail:
#     con.execute("INSERT INTO "+table_name+" VALUES(?, ?, ?)", (data[0], data[1], data[2]))
#     con.commit()


for val in student_detail2:
    con.execute("INSERT INTO "+table_name+" VALUES(:name, :rollno, :mobile)", {'name': val[0], 'rollno': val[1], 'mobile': val[2]})
    con.commit()

cur.execute("SELECT * FROM "+table_name)
data= cur.fetchall()

for i in data:
    print(i)

