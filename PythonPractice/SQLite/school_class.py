import sqlite3
import pdb

class school:
    def __init__(self,schooldb, stud_table, teach_table, other_staff_table):
        """
        :param schooldb:  this will be school database name
         """
        self.schooldb = schooldb
        self.con = sqlite3.connect(self.schooldb)
        self.cur = self.con.cursor()
        self.stud_table = stud_table
        self.teach_table = teach_table
        self.other_staff_table = other_staff_table

    def create_student_table(self, stud_id, name, standard):
        """
        :param stud_table: This will be a student table
        :param stud_id:
        :param name:
        :param standard:
        :return:
        """
        create_table_query = "CREATE TABLE {}({} TEXT, {} TEXT, {} INTEGER)".format(self.stud_table, stud_id, name, standard)
        try:
            self.con.execute(create_table_query)
        except Exception as e:
            pass
            print("Create Student Table Caught Exception :{}".format(e))


    def create_teacher_table(self, teach_id, name, subject):
        """
        :param teach_id:
        :param name:
        :param subject:
        :return:
        """
        create_table_query = "CREATE TABLE {}({} TEXT, {} TEXT, {} INTEGER)".format(self.teach_table, teach_id, name, subject)
        try:
            self.con.execute(create_table_query)
        except Exception as e:
            pass
            print("Create Teacher Caught Exception :{}".format(e))

    # CREATE OTHER STAFF TABLE WITH PRIMARY KEY
    def create_staff_table(self, staff_id, name, work):
        """
        :param staff_id:
        :param name:
        :param work:
        :return:
        """
        create_table_query = "CREATE TABLE {}({} TEXT PRIMARY KEY, {} TEXT, {} TEXT)".format(self.other_staff_table, staff_id, name, work)
        try:
            self.con.execute(create_table_query)
        except Exception as e:
            pass
            print("Create Staff Table Caught Exception :{}".format(e))


    def insert_student_data(self, stud_id, name, standard):
        """
        :param teach_id:
        :param name:
        :param subject:
        :return:
        """
        insert_query = "INSERT INTO {} VALUES(:stud_id, :name, :standard)".format(self.stud_table)
        select_query = "SELECT * FROM {} where stud_id=:stud_id".format(self.stud_table)
        try:
            self.cur.execute(select_query, {'stud_id':stud_id})
            data = self.cur.fetchall()
            # It will verify the student data exist with specific id or not.
            if data:
                print("Student ID Already Exist", stud_id)
            else:
                self.con.execute(insert_query, {'stud_id':stud_id, 'name':name, 'standard' :standard})
                self.con.commit()
                print("student data inserted successfully")
        except Exception as e:
            print("Insert Student Caught exception : {}". format(e))

    def insert_teachers_data(self, teach_id, name, subject):
        """
        :param teach_id:
        :param name:
        :param subject:
        :return:
        """
        insert_query = "INSERT INTO {} VALUES(?, ?, ?)".format(self.teach_table)
        select_query = "SELECT * FROM {} where teach_id=:teach_id".format(self.teach_table)
        try:
            self.cur.execute(select_query, {'teach_id':teach_id})
            data = self.cur.fetchall()
            # It will verify the student data exist with specific id or not.
            if data:
                print("Teacher ID Already Exist", teach_id)
            else:
                self.con.execute(insert_query, (teach_id, name, subject))
                self.con.commit()
                print("Teachers data inserted successfully")
        except Exception as e:
            print("Insert Teacher Caught exception : {}".format(e))

    # INSERT DATA INTO OTHER STAFF TABLE WITH PRIMARY KEY
    def insert_staff_data(self, staff_id, name, work):
        """
        :param staff_id:
        :param name:
        :param work:
        :return:
        """
        insert_query = "INSERT INTO {} VALUES(?, ?, ?)".format(self.other_staff_table)
        select_query = "SELECT * FROM {} where staff_id=:staff_id".format(self.other_staff_table)
        try:
            self.cur.execute(select_query, {'staff_id':staff_id})
            data = self.cur.fetchall()
            # It will verify the staff data exist with specific id or not.
            if data:
                print("Staff ID Already Exist", staff_id)
            else:
                self.con.execute(insert_query, (staff_id, name, work))
                self.con.commit()
                print("staff data inserted successfully")
        except Exception as e:
            print("Insert Staff Caught exception : {}".format(e))

    def get_student_data(self):
        select_query = "SELECT * FROM {}".format(self.stud_table)
        self.cur.execute(select_query)
        print(self.cur.fetchall())

    def get_teacher_data(self):
        select_query = "SELECT * FROM {}".format(self.teach_table)
        self.cur.execute(select_query)
        print(self.cur.fetchall())

    def get_other_staff_data(self):
        select_query = "SELECT * FROM {}".format(self.other_staff_table)
        self.cur.execute(select_query)
        print(self.cur.fetchall())

    def delete_student_record(self, stud_id):
        delete_query = "DELETE FROM {} where stud_id=:stud_id".format(self.stud_table)
        self.cur.execute(delete_query,{'stud_id':stud_id})
        self.con.commit()

    def delete_teacher_record(self, teach_id):
        delete_query = "DELETE FROM {} where stud_id=:stud_id".format(self.teach_table)
        self.cur.execute(delete_query,{'stud_id':teach_id})
        self.con.commit()


if __name__ == "__main__":
    obj = school('school2.db', 'student', 'teacher', 'staff')
    obj.create_student_table('stud_id', 'name', 'standard')
    obj.create_teacher_table('teach_id', 'name', 'subject')
    obj.insert_student_data('stud123', 'rahul', '12th')
    obj.insert_teachers_data('teach123', 'kalpesh', 'java')
    obj.get_student_data()
    obj.get_teacher_data()
    obj.delete_student_record('studx')
    obj.get_student_data()
    obj.create_staff_table('staff_id', 'name', 'work')
    obj.insert_staff_data('staff1', 'Mangesh', 'TeaWork')
    obj.get_other_staff_data()

