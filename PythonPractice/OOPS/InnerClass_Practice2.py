from InnerClass_practice import Student

class school(Student):

    def __init__(self, sch_name, sch_adress):
        self.sch_name = sch_name
        self.sch_adress = sch_adress
        self.obj = Student(2345, 'Rahul', 'pune', 23456, 'XII')

    def display(self):
        print(self.sch_name, self.sch_adress)
        print("__"*25)
        self.obj.show_info_detail()
        print("__" * 25)
        self.obj.show_detail()

    def get_method_detail(self):
        print(self.obj.__dir__())

    def get_city_name(self):
        print("1. Pune \n 2.Mumbai \n 3.Nagpur")
        user_input = input("Please Enter city Number")
        return int(user_input)

    def show_restaurant_detail(self):
        inputdata = self.get_city_name()
        if inputdata == 1:
            self.obj.pune_restaurant()
        if inputdata == 2:
            self.obj.mumbai_restaurant()
        if inputdata == 3:
            self.obj.nagpur_restaurant()


sch_obj = school('Convent', 'Pune')

#sch_obj.display()
#sch_obj.get_method_detail()
sch_obj.show_restaurant_detail()

