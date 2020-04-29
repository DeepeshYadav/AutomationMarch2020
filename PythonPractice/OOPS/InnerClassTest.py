global naveen
naveen = 10

class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lapy_obj = self.Laptop()

    def show_detail(self):
        print(self.name, self.rollno, naveen)
        self.lapy_obj.show_detail()

    class Laptop:

        def __init__(self):
            self.company = "HP"
            self.ram     = "2 GB"
            self.processor = "Corei3"

        def show_detail(self):
            print(self.company, self.ram, self.processor)




obj = student('rahul', 2345)

obj.show_detail()

obj2 = student.Laptop()

obj2.show_detail()