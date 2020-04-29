class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def inser_from_front(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = self.tail = new_node
            self.head.next = None
            self.tail.next = None
            self.head.prev = None
            self.tail.prev = None
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = self.tail = new_node
            self.head.next = None
            self.tail.next = None
            self.head.prev = None
            self.tail.prev = None
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.item, end=" ")
                n = n.next

    def insert_after_element(self,x, data):
        if self.head.item == x:
            new_node = Node(data)
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head = new_node
            self.head.prev = None
        else:
            n = self.head
            while n.next is not None:
                if n.item == x:
                    break
                n = n.next

            if n.next is None:
                print("Element does not exist in the list")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                new_node.prev = n



List1 = DoubleLinkList()

List1.insert_at_end(23)
List1.insert_at_end(45)
List1.insert_at_end(34)
List1.insert_at_end(22)
List1.inser_from_front(55)
List1.insert_after_element(34, 88)

List1.display_list()
