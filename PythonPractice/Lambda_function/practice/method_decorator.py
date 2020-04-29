######## Method Decorator ########

def method_decor(method):
    def inner(name_refer):
        if name_refer.name == "Deepesh":
            print("This is the same name we were expecting")
        else:
            method(name_refer)
    return inner

class Printing:
    def __init__(self, name):
        self.name = name

    @method_decor
    def get_name(self):
        print("Hello friend my name is:", self.name)

    def __call__(self, *args, **kwargs):
        print(self.name)
        for i in args:
            print(i)


obj = Printing("Megha")
obj.get_name()
obj(1, 2, 4, 5)

