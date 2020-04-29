class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        str = self.func()
        return str.upper()

@decorator
def greeting():
    return "good morning"

print(greeting())