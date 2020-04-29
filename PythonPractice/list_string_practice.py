list1 = [3, 6, 8, 9, 1]
       #[0, 1, 2, 3, 4]
       #[-5,-4,-3,-2,-1]
# get 0 position number
print(list1[0])
print(list1[4])

# Add data to the list with append method
# This method will add value at the end of list
list1.append(2)
print(list1)

#Remove specific value from list
list1.remove(6)
print(list1)

# Insert specific value in the  list

list1.insert(3, 10)
print(list1)

#find out max value from the list
print("max value:", max(list1))

# Find out mini value from the list
print("min vallue:", min(list1))

# sort the list, sort method sort the list in place
print("sorted", list1.sort())
print(list1)

#reverse the list, reverse method reverse the list in place
list1.reverse()
print(list1)

# list slicing
print(list1[1:])

print(list1[1:4])

# Negative index
print(list1[-2])

# Reverse with index
list2 = list1[::-1]
print(list2)
print(list1)
#print list with index jump
print(list1[::2])
print(list1[::-2])

print("#"*25)

# Extend the list
list3 = [4, 6, 8, 9]
list4 = [5, 2, 4, 1]

print(list4.extend(list3))
print(list4)

list5 = list4 + list3
print(list5)
print(list4)

print("#"*50)

# Shadow copy and Deep Copy

# Shallow Copy : It pass the refrence of the  list
list6 = [5, 7, 23, 45]
list7 = list6
list8 = list7
print(id(list6))
print(id(list7))
list7.append(56)
list8.append(100)
print("list6:", list6)
print("list7:", list7)
print("list8:", list8)


print("#"*50)
# Deep Copy :  Copy the whole list , not just passing the refrence

list9 = [4, 78, 55, 45]
list10 = list9.copy()
print("list9 :", id(list9))
print("list10 :", id(list10))
list10.append(200)
print("list9 ",list9)
print("list10 ",list10)


# Delete the list
# print("#"*50)
# list_temp = [3, 4, 6, 7]
# print(list_temp)
# del list_temp
# print(list_temp)

# Pop the element : It remove the element from the list and return he value
print("#"*50)

list_pop = [3, 6, 7, 8, 9]
print("list_pop :", list_pop)
list_pop_new = []
print(list_pop)
#data = list_pop.pop()
#print(data)
#print(list_pop)

# len method to get the length of any data, list, tuple, dictionary, string
list_length = len(list_pop)
for i in range(list_length):
    value = list_pop.pop()
    list_pop_new.append(value)

print("list_pop :", list_pop)
print("list_pop_new:", list_pop_new)



# 1. Get the square of each number of  the list
     # list = [5, 6, 8, 9]
     # output = [25, 3, 64, 81]
# 2. Get the sum of all the numbers of list
    # list = [4, 7 ,9 ,10]
    # output = 30
# 3. Check the type of ech element and append in an other list
    #-> list = [3, 6, 8, 'a', 2.5, [2, 5, 6]]
    # -> outlist = [int, int, int, str, float, list]

# 4. Separate out the even and odd number from the list.
    # list = [2, 5, 6, 8, 9, 12, 11]
    # list1 = [2, 6, 8, 12]
    # list2 = [5, 9, 11]

# 5. Get complete string from the list
    # list = ['hello', 'itpd', 'students', 'todays' , 'date', 26, 'june']
    # output = "hello itod students todays datet is 26 june"

