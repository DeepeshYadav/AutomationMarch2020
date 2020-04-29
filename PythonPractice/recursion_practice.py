"""
def get_sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

#print(get_sum([3, 5, 7, 9]))

def get_sum_recursion(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        return input_list[0] + get_sum_recursion(input_list[1:])


#print(get_sum_recursion([5, 7, 8, 9]))

def get_factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
        return  n*(get_factorial(n-1))

#print(get_factorial(5))

# Input = [2, 5, 6, [2, 3], [4, 8]]
total = 0

def get_sum_list_recu(input_list):
    total = 0
    print("first total_value:", total)
    for element in input_list:
        if type(element) == type([]):
            print("inside total_value:", total)
            total = total + get_sum_list_recu(element)
        else:
            total = total + element
    print(" outside total value:", total)
    return  total

print("total:", get_sum_list_recu([2, 5, 6, 7, [2, 3], [4, 1]]))


# 345 -> 543

# 345 = 12

############################################################

import datetime

#print today date

print(datetime.datetime.now())

# get year like 19
print(datetime.datetime.today().strftime("%y"))

# get year like 2019
print(datetime.datetime.today().strftime("%Y"))

# get month
print(datetime.datetime.today().strftime("%m"))

#
print(datetime.datetime.today().strftime("%M"))

# get today day
print(datetime.datetime.today().strftime("%d"))

# get week of the year
print(datetime.datetime.today().strftime("%W"))

# weekday of week
print(datetime.datetime.today().strftime("%w"))


import time
data = time.localtime()
print(data)
print(data[0])

for i in data:
    time.sleep(2) # wait for 2 secs
    print(i)
"""

import calendar
print(calendar.February)

print(calendar.month(2019,7))

print(calendar.isleap(2013))

output = calendar.calendar(2019)

print(output)

print(type(output[0]))
print("output:", output.split(""))
#print(output)