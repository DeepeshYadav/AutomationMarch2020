class A:
    def __init__(self, name, hard_disk, ram, cpu):
        self.c_name = name
        self.c_hard_disk = hard_disk
        self.c_ram = ram
        self.cpu =  cpu

    def show_method1(self):
        print(self.c_name, self.c_hard_disk, self.c_ram, self.cpu)

class B(A):

    # def __init__(self, c_name, c_hard_disk, c_ram):
    #     #super.__init__(self.name, self.hard_disk, self.ram, self.cpu)
    #     self.c_name = c_name
    #     self.c_hard_disk = c_hard_disk
    #     self.c_ram = c_ram
    #     #self.c_cpu = c_cpu

    def show_method(self):
        print("I am in child class")

obj = B('a', 'b', 'c', 'd')
obj.show_method()
obj.show_method1()