global gvar

gvar = "I am an outsider"

class ABC:
    """
    Class documents
    This is class document which is required to understand the code
    """
    classvar = "I am ABC class variable"
    global data
    data = 123

    # object method , which required refrence of class object, which is self
    def Config(self):
        print("We are inside config")
        print("Class Variable", ABC.var)
        print("Call Global Variable", gvar)

    def GetData(self):
        print("I am in Get data")

class XYZ:

    def show(self):
        print("My name is Khan")

# a = ABC()
# b = XYZ()
# Achine = "Forgote to get copy"
#
#
# ABC.Config(a)
#
# b.show()
# a.Config()
# a.GetData()
# print(a.var)
# print(ABC.var)
# print("Data", data)
#
# # Megical Methods
# print(a.__doc__)
# print(a.__dir__())