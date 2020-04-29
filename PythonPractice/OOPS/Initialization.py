class Computer:
    def __init__(self):
        print("I am inside init method")

    def spec(self):
        print("2 GB, 1TB, Corei5")


class Laptop:
    lapy_rank = 5
    print("lapy_rank", lapy_rank)
    def __init__(self, company, ram, processor):
        print("I am inside init method")
        self.company = company
        self.ram = ram
        self.processor = processor


    def show_detail(self):
        print("Company : {},  RAM : {}, Processor: {}".format(self.company, self.ram, self.processor))



#obj = Computer()
#obj.spec()

lap = Laptop("HP", "16GB", "Corei7")
lap1 = Laptop("Dell", "8GB", "Corei5")
lap2 = Laptop("Acer", "4GB", "Corei3")


lap.show_detail()
lap1.show_detail()
lap2.show_detail()

print(getattr(lap, 'lapy_rank'))

setattr(lap, 'lapy_rank', 10)

print(getattr(lap, 'lapy_rank'))

delattr(lap, 'lapy_rank')
#delattr(lap, 'lapy_rank')
print(getattr(lap, 'lapy_rank'))
print(hasattr(lap, 'lapy_rank'))
# print(lap.lapy_rank)
# lap.__setattr__('lapy_rank', 10)
# print(lap.lapy_rank)

# var = lap.__getattribute__('lapy_rank')
# print(var)
#lap.__delattr__('lapy_rank')

#var1 = lap.__getattribute__('lapy_rank')
#print("var1", var1 )

#print(lap.lapy_rank)

