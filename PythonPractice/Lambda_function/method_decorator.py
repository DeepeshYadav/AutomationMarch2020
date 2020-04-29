def check_greeting(method):
    def inner(input_ref):
        if input_ref.name != "ITPD":
            print("You are not allow in the class")
        else:
            method(input_ref)
    return inner

class greeting:
    def __init__(self, name):
        self.name = name

    @check_greeting
    def  print_gretting(self):
        print("Good Morning, ", self.name)

g = greeting("ITPD")
g.print_gretting()