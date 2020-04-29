class A:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_name(self, user_input: int):
        print("Name: {}, Address : {}, User Input :{}".format(self.name, self.address, user_input))

    def display_name(self, user_input : str):
        print("Name :", user_input)


    @staticmethod
    def static_data(n):
        fact =1
        for i in range(n, 1, -1):
            fact = fact*i
        return fact

    @classmethod
    def class_data(cls, number):
        if number > 1:
            flag = False
            for i in range(2, number):
                if number%i == 0:
                    #print("Its not Prime Number")
                    break
                else:
                    flag = True
                    #print("Its prime number")
        print("Its prime number") if flag is True else print("Its not an prime number")


    def compare(self, other):
        if self.name == other.name:
            return True
        else:
            return False

obj1 = A("Rahul", "Pune")
obj2 = A("Rahul", "Pune")

obj2.name = "Mohit"
if obj1.compare(obj2):
    print("Object are same")
else:
    print("Object are different")

#A.display_name(obj)
obj1.display_name(12345)
#print(obj.static_data(4))

#print(A.static_data(5))

#obj.class_data(11)


