def print_data(data):
    result = []
    for i in data:
        result.append(i**2)
    return result

print(print_data([1, 4, 7, 9]))

def generator_data(data):
    result = []
    for i in data:
        result.append(i ** 2)
    yield result


output = generator_data([3, 5, 7, 8])
print(next(output))
print(output.__next__())