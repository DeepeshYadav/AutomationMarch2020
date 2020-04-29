# In case of method oveloading recently defined method will be called
# In sense python does npt support method overloading

def sum(p, q , r):
    return p+q+r

def sum(a, b):
    return a+b


print(sum('4', '6'))
#print(sum(5, 7, 9))


"""
public static sum(int a, int b, int c)

public static sum(str a, str b)

"""