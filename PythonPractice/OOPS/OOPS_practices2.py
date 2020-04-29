from OOPS_practices import *


obj = A("Gandhi", 43)

class B:
    class_var = 234

    def __init__(self, address, rollno):
        self.address = address
        self.roll = rollno

    def show_age(self):
        obj.show_details()
        print("Address :{}, roll: {}".format(self.address, self.roll))


obj2 = B("Pune", 456)

obj2.show_age()



