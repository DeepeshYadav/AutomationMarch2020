def sum_of_list(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + sum_of_list(list1[1:])


#print(sum_of_list([2, 5, 7, 9]))

def sum_of_nested_list(input_list):
    total = 0
    for elem in input_list:
        if type(elem) == type([]):
            total = total + sum_of_nested_list(elem)
        else :
            total = total + elem
    return total

#print(sum_of_nested_list([2, 4, 5, [5, 6, 7], [7, 9]]))

def get_factorial(n):
    if n == 1:
        return n
    else:
        return n*get_factorial(n-1)

#print(get_factorial(5))

def get_fabonaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (get_fabonaci(n-1) + (get_fabonaci(n-2)))
print(get_fabonaci(7))

def fabonaci_series(n):
    a, b = 1, 2
    print(a, b)
    for i in range(n-2):
        a, b = b, a+b
        print(b, end=" ")


fabonaci_series(6)