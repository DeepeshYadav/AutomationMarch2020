"""
class Computer:

    def config(self):
        print("i5, 5RAM, 1TB")

com1 = Computer()

# Computer.config() ->  It will ask for

# call method by classname and passing object of class
Computer.config(com1)

# Call method by class object
# Behind the scene passing as object to the method
# self is the object calling itself
com1.config()
"""

