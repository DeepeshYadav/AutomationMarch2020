# Will continue from example , will solve same probplem using property decorator


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def msg(self):
        return self.name+" got the grade "+self.grade

    @msg.setter
    def msg(self, new_msg):
        sent = new_msg.split(" ")
        self.name = sent[0]
        self.grade = sent[-1]



obj = Student("Mohit", "B")
obj.msg = "Atriyo got the grade A"
print(obj.grade)
print(obj.name)
print(obj.msg)