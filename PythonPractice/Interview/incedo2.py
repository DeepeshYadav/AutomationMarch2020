"""
def decorator(func):
    def new_function():
        print("Extra Functionality")
        func()
    return new_function

@decorator
def initial_function():
    print("This is first functionality")

#initial_function()
def read_file(filename):
    with open(filename, 'r+') as file:
        data = file.read(5)
        yield data

for data in read_file('input.txt'):
    print(data)

def fibo(limit):
    a, b = 0, 1
    while a < limit:
         yield  a
         a, b = b, a + b

for i in fibo(20):
    print(i, end=" ")



class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def add_from_end(self, new_item):
        if self.head is None:
            new_node = Node(new_item)
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            new_node = Node(new_item)
            temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.item, end=" ")
                n = n.next


list1 = linkedList()

list1.add_from_end(20)
list1.add_from_end(34)
list1.add_from_end(40)

list1.print_list()

"""
import re
str1 = "a@b.com,   bsfaksdjfk;lj@test.com kjaklfjasjfakds thisis jklfjsa" \
       "b@v.com"


result = re.findall('\S+@\S+', str1)

print(result)