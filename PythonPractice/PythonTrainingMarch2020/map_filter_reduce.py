"""
# lambda function :

result = lambda x, y : x+y

print('lambda result :', result(20, 30))

#MAP

# square of each element
list1 = [3, 5, 7, 8, 9]

def odd_even(x):
    if x%2==0:
        return 'Even'
    else:
        return 'Odd'

#y = 30
#x = 11
#print(odd_even(y, x))


result_list = list(map(lambda i: i*2, list1))
print(result_list)

result_list2 = list(map(lambda nisha: odd_even(nisha), list1))
print(result_list2)

# list comprenhension

list2 = [3, 6, 7, 9, 2]
result3 = [x*x for x in list2 if x%2==0]
#print(result3)


# filter : it return value for which will get true answer

list3 = [3, 5, 7, 8, 9]
filter_result = list(filter(lambda x: x%2 == 0, list3))
print(filter_result)

# reduce : It return the result with end value

from functools import reduce

listn = [5, 7, 9, 2, 4]

sum_result = reduce(lambda x,y: x+y, listn)
print(sum_result)

import collections

print(dir(collections))

dict1 = collections.OrderedDict()

dict1['Saagr'] = 12345
dict1['Nisha'] = 34566
dict1['Smita'] = 34567

print(dict(dict1))


# how to convert two list into dictionary
list1n = [4 , 6, 8, 9, 3]
list2n = ['a', 'b', 'c', 'd']

print(dict(zip(list1n, list2n)))


# How does python manage the memory
# Python does memory management with heap data structure
"""

myset = set

listn3 = [2, 4, 5, 6, 2, 5, 7]

print(myset(listn3))

str1 = 'Hello How Are You, Hope you are doing good'
# List out all the unique characters from the strin

unique_list = []

for char in str1:
    if char not in unique_list:
        unique_list.append(char)
    else:
        continue

print(unique_list)

print(set(str1))

