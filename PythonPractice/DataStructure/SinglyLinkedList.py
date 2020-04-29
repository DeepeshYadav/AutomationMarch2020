class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def travers_list(self):
        if self.head is None:
            print("There is no element in the list")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next

    def add_element_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_element_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def insert_after_item(self, x, new_data):
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next

        if n.next is None:
            print("\n Element is not present in the list ")
        else:
            new_node = Node(new_data)
            new_node.next = n.next
            n.next = new_node


    def insert_before_element(self, x, input):
        #import pdb;pdb.set_trace()
        if x == self.head.data:
            new_node = Node(input)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            print(n.next.data)
            if n.next.data == x:
                break
            n = n.next

        if n.next is None:
            print("\n Element does not exist in the list")
        else:
            new_node = Node(input)
            new_node.next = n.next
            n.next = new_node
# n1 = Node(23)
# n2 = Node(4)


list1 = LinkedList()
# list1.head = n1
# list1.head.next = n2

list1.add_element_at_start(23)
# list1.add_element_at_start(34)
# list1.add_element_at_start(45)
# list1.add_element_at_start(50)
#
# list1.add_element_at_end(55)
list1.travers_list()
#
# list1.insert_after_item(34, 77)
# print("\n")
# list1.travers_list()
#
# # list1.insert_after_item(34, 56)
# # print("\n")
# # list1.travers_list()
#
# list1.insert_before_element(34, 89)
#
# print("\n")
# list1.travers_list()
#
# # print("\n")
# #list1.travers_list()
#
