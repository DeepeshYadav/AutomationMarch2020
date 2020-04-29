#while loop
# n= 1
# while n <= 10:
#     print(n)
#     if n%3 == 0:
#         print("This number is divided by 3:", n)
#         n = n + 1
#         break
#     else:
#         n = n + 1
#         continue
#
#

# while loop with nested if condition
#input = 123
#output = 321

#n = int(input("Please enter the number :"))
# revers = 0
# while n > 0:
#     var = n%10
#     revers = var + revers*10
#     n = n//10
#
# print(revers)
#
# #n=123, var = 3, revers = 3, n = 12
# #n = 12, var = 2, revers = 32, n = 1
# #n = 1, var = 1,  revers = 321, n = 0
#
#
# Nested if else condition

n = 20
for i in range(n):
    if i%3 == 0:
        if  i%5 == 0:
            print("This number is divisible of 5:", i)
        else:
            print("This number is not divisible of 5:", i)
    else:
        continue



