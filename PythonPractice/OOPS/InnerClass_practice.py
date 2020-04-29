class student_info:
    def __init__(self, address, mobileno, standard):
        self.address = address
        self.phone = mobileno
        self.standard = standard

    def show_info_detail(self):
        print(self.address, self.phone, self.standard)

class Student(student_info):
    #class variable
    stu_name = 'rahul123'
    stu_list = ['rahul', 'harish', 'teja', 'Rutuja']

    # constructor: which initialize the object of class
    def __init__(self, rollno, name, address, mobileno, standard):
        self.rollno = rollno #instance variable
        self.name = name
        super().__init__(address, mobileno, standard)
        # Inner class object
        self.inner_obj = self.laptop('Dell', '16 GB', 'Corei7')

    # instance method/object method
    def show_detail(self):
        print(self.rollno, self.name)
        self.inner_obj.show_detail_Inner()
        print(Student.stu_name)

    def pune_restaurant(self):
        print("Hello I am in Pune")

    def mumbai_restaurant(self):
        print("Hello I am in Mumbai")

    def nagpur_restaurant(self):
        print("Hello I am in Nagpur")

    @classmethod
    def getclassdata(cls):
        print(cls.stu_name)
        for stu in cls.stu_list:
            print(stu)

    @classmethod
    def achine_test(cls):
        print("My name is achine")

    @staticmethod
    def get_student_result(marks_list):
        for mark in marks_list:
            print(mark)

    # inner class
    class laptop:
        def __init__(self, brand, ram, processor):
            self.brand = brand
            self.ram = ram
            self.processor = processor

        def show_detail_Inner(self):
            print(self.brand, self.ram, self.processor)




obj = Student(2345, 'Rahul', 'pune', 23456, 'XII')
#inner_obj = Student.laptop('Dell', '10 GB', 'Corei7')
obj.show_detail()  # Child Class Method
Student.show_detail(obj)

# obj.show_info_detail() # Parent Class Method
#
# Student.getclassdata()
Student.get_student_result([30, 40, 50 ,60])
#
# inner_obj.shot_detail()
