"""

# List basics
# don't use list, ist in build keyword.

list1 = []

list1 = ['a', 1, 3.5, True, "TestString"]

list2 = [3, 6, 8, 9]

# Examples : [2, 6, 8, 9, 60]
# Indexing :  0, 1, 2, 3, 4
# Negative : -5, -4, -3, -2, -1

# list is mutable data type -> means we can add, delete, or modify
# Add element to the list -> append -> It will add element at the end of list

list2.append(10)

print(list2)

# Insert element at specific position:

new_list = [4, 6, 7, 8]
new_list.insert(2, 9)
print(new_list)


# Remove element from list -> We just need to provide the object that we want to remove

new_list = [4, 6, 7, 8]
new_list.remove(7)
print(new_list)

# print count of any object in the list
new_list = [4, 6, 7, 8, 4]
get_count = new_list.count(4)
print(get_count)



# pop the element from the list ->

new_list = [4, 6, 7, 8, 4, 12]
# pop with out index -> it removes the object from end of the list
result = new_list.pop()
print(result)
print(new_list)

# pop with index -> It removes the object from specific position.
result2 = new_list.pop(3)
print(result2)
print(new_list)


# remove element -> It never return removed the object
result3 = new_list.remove(4)
print(result3)
print(new_list)


# Add two list and extend and + operator works same.

list3 = [4, 6, 8]
list4 = [5, 7, 2]

list3.extend(list4)
print(list3)

list5 = list3 + list4
print(list5)

# Add list inside list

list1 = [3, 5, 7]
list2 = [2, 6, 8]

list3 = []

list3.append(list1)
list3.append(list2)
print(list3)

print(list3[0])
print(list3[1])

print(list3[1][1])


# slicing of list
new_list = [4, 6, 8, 9, 12, 45]

print(new_list[0: 3])
print(new_list[2::])
print(new_list[:-2])
print(new_list[:4])
print(new_list[::-1])


# Get index of specific object

new_list = [4, 6, 8, 5]
print(new_list.index(5))

# Deletion of list
del new_list
print(new_list)



# loop through the list element

new_list = [3, 5, 7, 45]
for elem in new_list:
    print(elem,":",new_list.index(elem))



# get square each number from the list and store another list
new_l1 = [1, 2, 3, 4, 5]
new_l2 = []

for elem in range(len(new_l1)):
    result = new_l1.pop(0)
    print(new_l1)
    print(result)
    new_l2.append(result**2)

print("list2 :", new_l2)
print("list1 :", new_l1)


# 6 April 2020
#1.write a program to get sum of all number in the given list
#list1 = [3, 5, 6, 7, 8]
#output = 29

new_list1=[3 , 5, 6 , 7 , 8]
number= 0
sum_num = 0
for element in new_list1:
    sum_num = sum_num + element

print("sum of this no:",sum_num)
print("sum of this list:", sum(new_list1))



# Reverse the list:

#sagar

#ragas

#
# In place reverse the list
list1 = [5, 7, 8, 9, 1]
result = list1.reverse()
print("result1 :", result)
print("list1 :", list1)


# does not reverse the list in place
list2 = [4, 6, 2, 8, 1]
result2 = list2[::-1]
print("result2:", result2)
print("list2:", list2)

print(list1)

################ Sorting of List #####################
# sort method , sort the list in place and does not return anything.
list1 = [2, 4, 6, 7, 1, 8]
result = list1.sort()
print(result)
print(list1)

#### max value from the list
print(max(list1))

### minimum value from the list
print(min(list1))

### sum of the list
print(sum(list1))
###multiplication of the list


# deep copy and shallow copy

list1 = [2, 6, 8, 9]
list2 = list1  # shallow copy, it pass the refrence or memory address
list4 = list2
list2.append(23)
list4.append(45)
print("address list1:", id(list1))
print("address list2:", id(list2))
print("address list4:", id(list4))

print("list1:", list1)
print("list2:", list2)
print("list4:", list4)

print("#"*50)

list3 = list1.copy()# deep copy, it pass values of list , but not the address
list5 = list3.copy()
print("address list1:", id(list1))
print("address list3:", id(list3))
print("address list5:", id(list5))

list3.append(25)
list5.append(88)
print("list1:", list1)
print("list3 :", list3)
print("list5 :", list5)

"""

############################################


lista = [4, 6, 8, 9]
listb = lista
listc = lista + listb
listb.append(34)
listd = listb

print("lista:", lista)
print("listd:", listd)
print("listc:", listc)


def list_function():
    lista = [4, 6, 8, 9]
    listb = lista
    listc = lista + listb
    listb.append(34)
    listd = listb

    print("lista:", lista)
    print("listd:", listd)
    print("listc:", listc)



list_function()