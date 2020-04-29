def function1(data):
    for i in data:
        print(i*i, end=" ")


#function1([2, 4, 5, 6, 7])

def generator_fun2(data):
    for j in data:
        yield j*j

output = generator_fun2([3, 6, 8, 9])
print(output)

# print(output.__next__())
# print(output.__next__())
# print(output.__next__())
# print(next(output))

for value in output:
    print(value)

