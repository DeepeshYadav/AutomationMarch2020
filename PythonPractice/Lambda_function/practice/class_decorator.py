class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        str1 = self.func()
        return str1.upper()

@Decorator
def gritting():
    return "good morning"


print(gritting())
