class check:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        if  b == 0 :
            return "Please user appropriate denominator"
        else:
            return self.func(a, b)

@check
def div(a, b):
    return (a/b)


print(div(4, 0))