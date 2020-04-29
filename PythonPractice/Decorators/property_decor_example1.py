# In this class will how to set values using setter
# and next example2 will explain how achieve this using @propert decorator

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    def msg(self):
        return self.name +" got the grade "+self.grade

    def setter(self, msg):
        sent = msg.split(" ")
        self.name = sent[0]
        self.grade = sent[-1]






obj = Student('Amey', 'A')
obj.setter("Rahul got the grade B")
print(obj.name)
print(obj.grade)
print(obj.msg())

