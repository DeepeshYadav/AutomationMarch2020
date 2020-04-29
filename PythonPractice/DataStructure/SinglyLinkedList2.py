class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkList:
    def __init__(self):
        self.head = None


    def travers_list(self):
        if self.head is None:
            print("No Element in the list")
            return
        else:
            n = self.head
            while n is not None:
                print(n.item, end=" ")
                n = n.ref


    def add_element_at_end(self, elem):
        if self.head is None:
            new_node = Node(elem)
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref

            new_node = Node(elem)
            n.ref = new_node
            new_node.ref = None

    def add_element_to_start(self, elem):
        if self.head is None:
            new_node = Node(elem)
            self.head = new_node
        else:
            new_node = Node(elem)
            new_node.ref = self.head
            self.head = new_node


    def add_element_after_target(self, x, elem):
        #import pdb; pdb.set_trace()
        n = self.head
        while n.ref is not None:
            if n.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("Element does not exist in the list")
        else:
            new_node = Node(elem)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_target(self, x, elem):
        n = self.head
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print(" \n Element does not exist in the list")
        else:
            new_node = Node(elem)
            new_node.ref = n.ref
            n.ref = new_node

    def search_element_in_list(self, x):
        n = self.head
        while n.ref is not None:
            if n.item == x:
                return True
            n = n.ref

        if n.ref is None:
            return False

    def count_total_element(self):
        n = self.head
        count = 0
        while n.ref is not None:
            count = count + 1
            n = n.ref
        return count

    def delete_from_start(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.ref

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

List1 = LinkList()
List1.add_element_at_end(10)
List1.add_element_at_end(20)
List1.add_element_at_end(50)
List1.add_element_at_end(60)
List1.add_element_to_start(30)

List1.travers_list()
List1.add_element_after_target(20, 70)

print("\n")
List1.travers_list()

List1.insert_before_target(20, 55)

print("\n")
List1.travers_list()

# print("\n", List1.search_element_in_list(10))
#
# print("\n", List1.search_element_in_list(80))
#
# print("\n", List1.count_total_element())

List1.delete_from_start()

print("\n")
List1.travers_list()
List1.delete_from_end()

print("\n")
List1.travers_list()