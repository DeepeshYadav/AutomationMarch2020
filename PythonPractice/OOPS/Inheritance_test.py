""""
class laptop:
    def get_config(self):
        print(" 2 GB RAM, 1TB, corei3")

class Computer(laptop):
    def show_detail(self):
        print("1 GB,  dual core, 500 GB")

obj = Computer()
obj.get_config()
obj.show_detail()



######################################################################
# Multi Level Inheritance

class ABC:
    abc_var = 10
    def get_config(self):
        print(" 2 GB RAM, 1TB, corei3")

    def print_class_name(self):
        print(self.__dir__())

class XYZ(ABC):
    def show_detail(self):
        print("1 GB,  dual core, 500 GB")

    def print_class_name(self):
        print(self.__dir__())


class PQR(XYZ):
    def get_detail(self):
        print("1 GB,  dual core, 500 GB")

    def print_class_name(self):
        print(self.__dir__())

a= ABC()
x=XYZ()
p=PQR()

ABC.get_config(a)
a.get_config()
print(a.__dir__())
print(a.__class__)

print(hasattr(a, 'abc_var'))
print(getattr(a, 'abc_var'))
a.print_class_name()

x.get_config()
x.show_detail()
x.print_class_name()


p.abc_var
p.show_detail()
p.get_config()
p.print_class_name()

#########################################################
# Multiple Inheritance

class ITPD():
    def __init__(self, name, rollno, address, mobile=None):
        self.name = name
        self.rollno = rollno
        self.address = address
        self.MobileNumber = mobile
    def show_stud_detail(self):
        print("Name: {}, rollNo : {}, address: {}, MobileNo : {}". format(self.name, self.rollno, self.address, self.MobileNumber))
        print(self.__class__)
        print("Hello I am an ITPD student")

    def ITPD_June(self):
        print("We are ITPD June batch student")

class Qspider():
    def __init__(self, name, rollno, address, mobile=None):
        self.name = name
        self.rollno = rollno
        self.address = address
        self.MobileNumber = mobile

    def show_stud_detail(self):
        print("Name: {}, rollNo : {}, address: {}, MobileNo : {}". format(self.name, self.rollno, self.address, self.MobileNumber))
        print(self.__class__)
        print("Hello I am a Qspider student")

    def Q_June(self):
        print("Hello We are Q spider JUne batch student")

class ITComp(Qspider, ITPD):
     def get_student_detail(self):
         print("Get Student Details")

obj1 = ITComp('harish', 345, 'pune', 67894)
obj1.show_stud_detail()
obj1.ITPD_June()


"""
#################################
# Use of super keyword

class Games():
    def __init__(self, carrom, chase):
        self.carrom = carrom
        self.chase = chase

    def show_games(self):
        print("Indoore Game1: {}, Indoore Game2: {}".format(self.carrom, self.chase))


class Indoore(Games):
    __mydata = 123
    harish_age = 23
    def __init__(self,  caroom, chase, ludo, cards):
        super().__init__(caroom, chase)
        self.ludo = ludo
        self.cards = cards

    def show_games(self):
        print("Indoore Game1: {}, Indoore Game2: {}".format(self.carrom, self.chase))
        print("Indoore Game3: {}, Indoore Game4: {}".format(self.ludo, self.cards))




obj = Indoore(4, 8, 4, 6)
obj.show_games()
print(obj._Indoore__mydata)
print(obj.harish_age)
# obj2 = Games(4, 6)
# obj2.show_games()