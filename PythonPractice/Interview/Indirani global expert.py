# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_from_start(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def display_list(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.item)
#                 n = n.next
#
#
# list1 = LinkedList()
#
# #list1.insert_from_start(45)
# list1.insert_from_start(34)
# # list1.insert_from_start(32)
# # list1.insert_from_start(23)
#
# list1.display_list()



#lambda
# from functools import reduce
# list1 = [3, 5, 6, 7, 8]
#
# result = list(map(lambda x : x*x, list1))
# print(result)
#
# result1 = list(filter(lambda x : x%2 == 0, list1))
# print(result1)
#
# result3 = reduce(lambda x, y :  x+y , list1)
# print(result3)

import re
str1 = """
hello@test.com and other email
like data@gmail.com
will send mail deepesh.yadav@calsoftinc.com
"""


result = re.findall("[a-zA-Z._]+@+[a-zA-Z._]+", str1)
result2 = re.findall('\S+@\S+', str1)

print(result)
print(result2)