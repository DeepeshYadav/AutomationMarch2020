"""
class A:
    __class_var = 30
    def __init__(self, name, address, rollno):
        self.name = name
        self.address = address
        self.rollno = rollno
        self.__class_var = self.__class_var + 1

    def display(self):
        return self.name, self.address, self.rollno

    def show(self):
        print(f"Users details Name : {self.name}, Address : {self.address}, Rollno : {self.rollno}")

class B():
    def __init__(self, parts, stock):
        self.parts = parts
        self.stock = stock

    def display(self):
        return self.parts, self.stock

class C(A, B):
    def show(self):
        print("I am in class c")

    # def show(self):
    #     print("This is class C show method.")


obj_c = C("Rahul", "Indore The Cool Place", 234)
obj_c.show()
obj_a = A("Rahul", "Indore The Cool Place", 234)
A.show(obj_a)
"""

print(str.__add__("Deepesh ", "Yadav"))
print(int.__add__(34, 45))

def get_generator(low, high):
    while low <= high:
        yield  low
        low += 1


for value in get_generator(5, 10):
    print(value, end="")


def add_number(num):
    def adder(number):
        return number+num
    return adder

add = add_number(10)
print(add(21))


def griting(func):
    def wrapper(*args):
        name = func(*args)
        return f"Hello Good Morning: {name}"
    return wrapper


@griting
def display(name):
    return name

#print(display('Rahul'))


class Mydecorator():
    def __init__(self, function):
       self.function = function


    def __call__(self, *args, **kwargs):
        print("Hello This is class decorator")
        self.function(*args,  **kwargs)
        print("Hello This is end msg of class decorator")



@Mydecorator
def show_msg(name, message="Good Monrning"):
    print(f"Hey {name}, {message}")


show_msg("Mayank")



import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))