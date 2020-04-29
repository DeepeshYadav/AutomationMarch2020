"""
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            temp = self.head
            while temp.next is not None:
                #import pdb;pdb.set_trace()
                print(temp.item, end=" ")
                temp = temp.next

    def add_item_from_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


list1 = Linkedlist()
list1.add_item_from_start(24)
list1.add_item_from_start(23)
list1.add_item_from_start(34)
list1.add_item_from_start(45)
list1.add_item_from_start(36)
list1.print_list()
"""

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class SinglyLinkedlist:
    def __init__(self):
        self.head = None


