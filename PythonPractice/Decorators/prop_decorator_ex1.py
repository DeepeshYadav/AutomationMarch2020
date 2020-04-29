"""
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        #self.email = self.firstname + "." + self.lastname + "@gmail.com"

    def email(self):
        return self.firstname+"."+self.lastname+"@gmail.com"


obj = Student('Rahul', 'Shinde')
obj.firstname = 'Achine'
print('Firstname :', obj.firstname)
print('Lastname :', obj.lastname)
print('Email', obj.email())

"""

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        #self.email = self.firstname + "." + self.lastname + "@gmail.com"

    @property
    def email(self):
        return self.firstname+"."+self.lastname+"@gmail.com"


    def setter(self, user_input):
        data = user_input.split(" ")
        self.firstname = data[0]
        self.lastname = data[1]


obj = Student('Rahul', 'Shinde')




print('Email:', obj.email)
#obj.firstname = 'Achine'
#obj.lastname = 'Talole'

input_msg = "Harish rathod is doing good job"
obj.setter(input_msg)
print('Firstname :', obj.firstname)
print('Lastname :', obj.lastname)
print('Email:', obj.email)

