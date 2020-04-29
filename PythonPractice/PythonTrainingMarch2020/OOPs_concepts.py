# class : class is nothing but a blue print with certain properties and Though which we can
#         create multiple objects

# object : Object is real copy of class through which we can access class properties.

# Method : any function is by default a method in object oriented programming.

# Inheritance
# Polymorphism
# Incapsulation /Abstraction

#------------------------------------------------

# Example with Default constructor
"""
class Car:
    # constructor is use for to allocate memory/initiliase  the object of class
    def __init__(self):
        print("We are in default constructor")

    # Instance Method
    def car_name(self):
        print("Car name is Swift")


obj = Car()
obj.car_name()


# Example with parametize constructor
class Car:

    #class variable
    car_speed = 220

    # constructor is use for to allocate memory/initiliase  the object of class
    def __init__(self, name):
        print("We are in paramitize constructor")
        # instance variable
        self.car = name

    # Instance Method
    def car_name(self):
        return f"Car name :{self.car}"


obj1 = Car('Alto')
obj2 = Car('Swift')
obj3 = Car('WagonR')

print(obj1.car_name())
print(obj1.car_speed)
print(Car.car_name(obj1))

print(obj2.car_name())
print(obj2.car_speed)
print(Car.car_name(obj2))

print(obj3.car_name())
print(obj3.car_speed)
print(Car.car_name(obj3))

#############################################################
# Inheritance : Aquaire the property of one class into another class is know as inheritance.

# Singleton Inheritance
# Class1 -> Class2

class Animal:
    def __init__(self, name, catogary):
        self.name = name
        self.catogary = catogary

    def show_details(self):
        print(f"Animal Name :{self.name}, Catogary : {self.catogary}")

class Wild(Animal):

    def __init__(self, name, catogary, voice):
        super().__init__(name, catogary)
        self.voice = voice

    def display_detail(self):
        print(f"Name {self.name}, 'Catgory' {self.catogary}, Voice : {self.voice}")




wobj = Wild('Dog', 'Pat Animal', 'Barking')

wobj.show_details()

wobj.display_detail()



######################################################################################

# Multi Level Inheritance
# Class1 -> Class2 -> Class3
# Dadaji -> PAPA -> Son

class Animal:
    def __init__(self, name, catogary):
        self.name = name
        self.catogary = catogary

    def show_details(self):
        print("_" * 50)
        print("We are in Animal class")
        print(f"Animal Name :{self.name}, Catogary : {self.catogary}")

class Wild(Animal):

    def __init__(self, name, catogary, voice):
        super().__init__(name, catogary)
        self.voice = voice

    def display_detail(self):
        print("_" * 50)
        print("We are in Wild class")
        print(f"Name {self.name}, 'Catgory' {self.catogary}, Voice : {self.voice}")


class Circus(Wild):
    def __init__(self, name, catgory, voice, skill):
        super().__init__(name, catgory, voice)
        self.skill = skill


    def CirCus_Event(self):
        print("_"*50)
        print("We are in Circus Event")
        print(f"Name: {self.name} \n")
        print(f"catgory: {self.catogary} \n")
        print(f"voice: {self.voice} \n")
        print(f"Skill: {self.skill} \n")


wobj = Circus('Elephant', 'wild Animal', 'Roaring', 'Dance')

wobj.show_details()

wobj.display_detail()

wobj.CirCus_Event()



########################################################################################
#Mupltiple Inheritance

# Class1 and Class2 -> Class 3

class A:
    def __init__(self, name, address):
        self.name = name
        self.address = address


    def display(self):
        print("--" * 50)
        print("We are in Class A")
        print(f"Name : {self.name} , Address : {self.address}")


class B :
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def displayB(self):
        print("--" * 50)
        print("We are in Class B")
        print(f"Name : {self.name} , Address : {self.address}")

    def Gretting(self):
        print("--" * 50)
        print("We are in Class B")
        print(F"Hello {self.name}, How are you")

# Method Resolution Order (MRO): If both parent class have same method name, as per order method name will be called
# In below example shows Class A and Class B , both have display method
# While creating object of Class C and try to access display method , then display method of class A will be called
# As per order.
class C(A, B):
    def __init__(self, name, address, company, city):
        super().__init__(name, address)
        self.company = company
        self.city = city

    def show(self):
        print("--"*50)
        print("We are in Class C")
        print(f"Name : {self.name} , Address : {self.address}, company : {self.company}, city : {self.company}")


objc = C('Rahul', 'Sangamwadi', 'IBM', 'Pune')
objc.display()
objc.displayB()
objc.show()
objc.Gretting()

objb = B('Sachine', 'Mumbai')
objb.displayB()
objb.Gretting()

"""

