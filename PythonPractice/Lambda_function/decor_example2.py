#1. FUnction as argumenet
#2. Function inside a function inner function.
#3. Function refrence


def check_div(func):
    def inner(p, q):
        if p < q or q == 0:
            return "Can't devide ,please use appropriate number to divide"
        else :
            return func(p, q)
    return inner


@check_div
def div(a, b):
    return a/b

#div = check_div(div)

print(div(4, 2))