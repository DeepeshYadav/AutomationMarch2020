# Polymorphism
# Incapsulation /Abstraction
# Polymorphism : Poly -> Many, Morphis -> Form
'''
# Operator Overloading
a = 10
b = 20

x= 'abc'
y = 'xyz'

print(a+b)
print(x+y)

print(str.__add__(x, y))

print(int.__add__(a, b))

#Magical Methods.

str.__add__()
str.__mul__()
str.__dir__()
str.__doc__


# Function oveloading : same name function with different output



def addition(x, y):
    return x + y

def addition(a, b, d):
    c = a + b + d
    result = c//2
    return result

print(addition('Rahul', 'Jain'))


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # Overloading is not possible in python , it consider only latest defined mathod.
    def display(self):
        return f'Name : {self.name}, Roll : {self.roll}'

    def display(self):
        return f'Name : {self.name}'



if __name__ == '__main__':
    obj = Student('Rahul', 'ABC5456')
    print(obj.__module__)
    print(obj.display())


# Method Overiding : Its same method is two different class which are parent and child of each other.

class computer:
    def __init__(self, company, ram, cpu):
        self.company = company
        self.ram = ram
        self.cpu = cpu


    def display_detail(self):
        return f"Comp_name : {self.company}, RAM: {self.ram}, CPU : {self.cpu}"


class DELL(computer):

    def __init__(self, processor, CPU ='200MHZ'):
        self.processor = processor
        self.CPU = CPU

    def display_detail(self):
        print(f"Processor : {self.processor}, CPU: {self.CPU}")



if __name__ == '__main__':
    obj = DELL('CoreI3')
    obj.display_detail()

    obj2 = computer('Asus', '4GB', '200GMHZ')
    print(obj2.display_detail())



# Incapsulation/ Data hiding / Abstraction = Hiding the data to access out side of the class
# Single UnderScore
# Double Underscore
class Company:

    def __init__(self, name, id, salary):
        self.name = name
        self._id = id
        self.__salary = salary


    def show_details(self):
        print(self.name, self._id, self.__salary)



    def _show_id(self):
        return self._id

    def __show_salary(self):
        return  self.__salary


if __name__ == '__main__':
    obj = Company('Rahul', 3456, 50000)
    obj.show_details()
    print(obj.name)
    print(obj._id)
    print(dir(obj))
    print(obj._Company__salary)

    print(obj._show_id())

    print(obj._Company__show_salary())


# Decorator : Decorator add new functionality in your existing code.

def greeting(func):
    def show_gretting():
        print("Hello, Good Morning."
              "How are you.")
        func()
    return  show_gretting


@greeting
def print_name():
    print("Rahul")


print_name()


class College():
    management = 2000
    def __init__(self, cname, area, course):
        self.cname =cname
        self.area = area
        self.course = course

    def show_detail(self):
        return  f"College Name: {self.cname}, Area : {self.area}, course: {self.course}"

    # class method intract with class varible only not instance variable.
    @classmethod
    def manage_data(cls):
        print(cls.management)

    # static method does not relate with any class variable or method
    @staticmethod
    def fabonaci(number):
        a, b = 0, 1

        while a < number:
            print(a, end= " ")
            a , b = a + b , a


if __name__ == '__main__':
    obj = College('SIMS', 'Pune', 'Btech')
    print(obj.show_detail())
    obj.manage_data()
    obj.fabonaci(20)
'''


class College():
    management = 1000
    def __init__(self,cname,area,course):
        self.cname = cname
        self.area = area
        self.course = course
    def show_detail(self):
        return f"College Name:{self.cname}, Area:{self.area}, Course:{self.course}"

    @classmethod
    def manage_data(cls):
        print(cls.management)

    @staticmethod
    def fibonacci_series(number):
        a,b=0,1
        while a < number:
            print(a,end=" ")
            a,b=a+b,a

if __name__ == '__main__':
    obj = College('IICC','Ravi Nagar','MCA')
    print(obj.show_detail())
    obj.manage_data()
    obj.fibonacci_series(20)