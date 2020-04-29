from functools import reduce

result = reduce(lambda x , y : x+y, [3, 6, 8, 9])
result2 = reduce(lambda x , y : x*y, [3, 6, 8, 9])


print(result)
print(result2)