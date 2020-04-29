# Polymorphism
# Incapsulation /Abstraction
# Polymorphism : Poly -> Many, Morphis -> Form

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

################################################################
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
#######################################################################

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
        print(f"Processor : {self.processor}, company: {self.CPU}")



if __name__ == '__ main__':
    obj = DELL('CoreI3')
    output = obj.display_detail()
    print(output)
