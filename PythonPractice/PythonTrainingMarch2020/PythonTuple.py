#Tuple is similar like a list, but it is immutable

tuple1 = (2, 5, 7, 8, 9, 4, 5)
#         0  1  2  3  4  5

"""
print(tuple1[0:4])

print(tuple1.index(8))

print(tuple1.count(5))


# print each value
for value in tuple1:
    print(value, end=" ")
"""

# odd numbers from the tuple
for i in tuple1:
    if i%2 != 0:
        print("odd :", i)
    else:
        print("even :", i)



