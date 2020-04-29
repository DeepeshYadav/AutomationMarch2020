class A:
    class_var = 234

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print("Age :{}".format(self.age))

    def show_details(self):
        print("Name :{}".format(self.name))
        self.show_age()

    @classmethod
    def class_data(cls):
        obj = A("daya", 34)
        obj.show_details()
        print(cls.class_var)

    @staticmethod
    def my_static_details():
        print(" We are static methods")


#obj = A('rahul', 28)
# obj.show_details()
#A.class_data()
# A.my_static_details()

