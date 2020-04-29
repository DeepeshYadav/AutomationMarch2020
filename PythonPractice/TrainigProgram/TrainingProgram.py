#
# """
# list2 = [4, 6,  8, 9, 23]
#
# result = list(map((lambda x : (x%2==0)), list2))
# print(result)
#
# result2 = list(filter((lambda x : (x%2==0)), list2))
# print(result2)
#
#
# from functools import reduce
# result = reduce((lambda x, y : x + y), list2)
# print(result)
#
# y_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]
# result13 = list(filter(lambda x: x%13 == 0, y_list))
# print(result13)
#
# string_list = ['geek', 'aba', 'keek', 'adada', 'subway', 'ab']
#
# result_rever = list(filter(lambda x : (x == "".join(reversed(x))), string_list))
#
# print(result_rever)
#
#
#
# def read_large_file(filepath,  blocksize):
#     with open(filepath, 'rb') as file:
#         while True:
#             data = file.read(blocksize)
#             if data:
#                 yield data
#             else:
#                 return
#
#
# # for data in read_large_file('filename1.txt', 256):
# #     print("\n", data)
#
#
# #--------------------------------------------------
#
# def file_operation(filename):
#     with open(filename, 'r+') as file:
#         # data = file.read()
#         # file.seek(0, 0)
#         # file.write("New Data")
#         data = file.read(200)
#         file.seek(0, 1)
#         file.write("middle Location and Its confirmation")
#         #print(data)
#         file.seek(0, 2)
#         file.write("New Location and Its confirmation")
#         print(file.tell())
#
# def file_operation_1(filename):
#     with open(filename, 'r+') as file:
#         data = file.read()
#         file.write("New Data")
#         print(data)
#
#
# #file_operation('filename1.txt')
#
#
# def file_exchange_line():
#     with open('filename3.txt', 'r+') as file3:
#         file3_lines = file3.readlines()
#
#         print("file3:",file3_lines)
#
#     with open('filename2.txt', 'r+') as file2:
#         file2_lines = file2.readlines()
#         print("file2:",file2_lines)
#
#         for i in range(2, 5):
#             file3_lines.insert(i, file2_lines[i])
#
#         print("file3:", file3_lines)
#     with open('filename4.txt', 'a+') as file4:
#         for line in file3_lines:
#             file4.write(line)
#
# #file_exchange_line()
# import time
# def tail_command(filepath, n):
#     pre_len = 0
#     while True:
#         with open(filepath, 'r') as file:
#             lines = file.readlines()
#             #print(lines)
#             if pre_len < len(lines):
#                 for i in range(-n, 0, 1):
#                     print(lines[i])
#                 pre_len = len(lines)
#             else:
#                 continue
#         time.sleep(10)
# #tail_command('filename4.txt', 4)
#
# list1 = [3, 6, 8, 45, 35, 9, 0, 34]
#
# print(list1[1:4])
#
# print(list1[:5])
# print(list1[2::])
#
# max = list1[0]
#
# for i in list1:
#     if i > max:
#         max=i
# print(max)
# """
#
# # reverse string
# def reverse_int(n):
#     revr_num = 0
#     while n > 0:
#         num = n%10
#         revr_num = revr_num * 10 + num
#         n = n//10
#     print(revr_num)
#
# #reverse_int(2345136)
#
# list1 = [2, 6, 7, 8, 23]
# list2 = list1
# print(list2)
# list2.append(5)
# print(list1, list2)
#
# list3 = list1.copy()
#
# list3.append(45)
# print(list1, list3)
#
# import os
#
# datalist = os.listdir(".")
# print(datalist)
#
# data_dict = {}
#
# for data in datalist:
#     finename, extension = data.split(".")[0], data.split(".")[1]
#     if extension in  data_dict:
#         data_dict[extension] += 1
#     else:
#         data_dict[extension] = 1
# print(data_dict)

def is_prime_number(input):
    count = 0
    for n in range(2, input):
        if (n%3 ==0 or n%2==0 or n%5==0 or n%7==0) and (n not in [2, 3, 5, 7]):
            continue
        else:
            print(n, end=" ")
            count += 1
    print(": Total Count :", count)

is_prime_number(100)
#-------------------------------------
#list comphension
# list1 = [3, 6, 8, 9, 23, 56]
# result = list(map(lambda x : (x%2 != 0), list1))
# odd_result = list(filter(lambda x : x%2 == 0, list1))
#
# print(result)
# print(odd_result)
#
# multi = [x*2 for x in list1 if x < 50]
#
# print(multi)
#
# dict1 = {'a':3, 'b':34, 'c':45, 'd':56 }
#
# result = {k:v*2 for k, v in dict1.items()}
#
# print(result)
#
#
#------------------------------------------------

def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("{0} This is leap year".format(year))
            else:
                print("{0} This is not leap year".format(year))
        else:
            print("{0} This is leap year".format(year))
    else:
        print("{0} This is not leap year".format(year))


#leap_year(2025)

def factorial_data(n):
    fact=1
    for i in range(1, n+1):
        fact = fact*i
    return fact

#print(factorial_data(5))

def fabonaci_series(n):
    a, b = 1, 2
    for i in range(n):
        a ,b = b, a+b
        print(a, end=" ")

#fabonaci_series(10)
import re
def get_all_the_email():
    with open('filename4.txt', 'r+') as file:
        data = file.read()
    result_email = re.findall(r'[a-z0-9A-Z._]+@[a-z0-9A-Z.]+', data)
    print(result_email)
    result_number = re.findall(r'\d{3}-\d{3}-\d{4}', data)
    print(result_number)

#get_all_the_email()
import array as arr
def get_array_access():
    newarray = arr.array('i', [2, 5, 7,  8, 'r'])
    print(newarray)

get_array_access()