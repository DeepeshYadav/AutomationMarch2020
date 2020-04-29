def example1():
    data = lambda x : x**2
    print(data(8))

example1()

list2 = [3, 5, 7, 8, 9, 6, 10]
data = list(map((lambda x:x**2), list2))
print(data)

result = list(filter((lambda X: (X%2 != 0)), list2))
print(result)

from functools import reduce
result2 = reduce((lambda x, y: x + y), list2)

print(result2)