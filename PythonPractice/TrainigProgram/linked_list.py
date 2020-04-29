class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail =  None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add_fisrt(self, e):
        newest = self.Node(e)
        if self.is_empty():
            self.head = newest
            self.tail = newest

list1 = Linkedlist()
list1.head = Node(2)
second = Node(34)
third = Node(23)
four = Node(26)

list1.head.next = second
second.next = third
third.next = four
list1.print_list()


