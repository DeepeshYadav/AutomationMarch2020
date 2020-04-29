"""
import os
class GetCount:
    def __init__(self, path):
        self.path = path

    def get_files_directories_count(self):
        fcount = 0
        dcount = 0
        datalist = os.listdir(self.path)
        for data in datalist:
            if os.path.isfile(os.path.join(self.path, data)):
                fcount += 1
            elif os.path.isdir(os.path.join(self.path, data)):
                dcount += 1
            else:
                continue
        return fcount, dcount

    def get_pdf_file_count(self):
        pdf_count = 0
        datalist = os.listdir(self.path)
        for data in datalist:
            if os.path.isfile(os.path.join(self.path, data)):
                if data.split(".")[-1] == "pdf":
                    pdf_count += 1
                else:
                    continue
            else:
                continue
        return pdf_count

if __name__ == "__main__":

    obj = GetCount("C:\\TestData")
    print("Files count : ", obj.get_files_directories_count()[0])
    print("Directoris count : ", obj.get_files_directories_count()[1])
    print("PDF file count :", obj.get_pdf_file_count())


class ABC:
    #
    # This is class is for practice parpous and
    # will go through all the concept of class
    #
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __dispay(self):
        return f'name: {self.name}, address : {self.address}'


    def show(self):
        return f'name: {self.name}, address : {self.address}'


class xyz(ABC):
    __number = 23456
    def __init__(self, name, address, city, company):
        super().__init__(name, address)
        self.city = city
        self.company = company
        self._good = 'good'
        self.__exellent = 'execllent'

    def display(self):
        return f'name: {self.name}, address : {self.address}, ' \
            f'city : {self.city}, company : {self.company}'

    @classmethod
    def display_class(cls, num):
        n = cls.__number
        print(n)
        reverse = 0
        while num > 0:
            temp = num%10
            reverse = reverse*10 + temp
            num = num//10
        return reverse

    @staticmethod
    def get_prime_number(number):
        prime = []
        for n in range(2, number):
            if (n%2 == 0 or n%3 == 0 or n%5== 0 or n%7==0) and (n not in [2, 3, 5, 7]):
                continue
            else:
                prime.append(n)
        return prime





# obj = ABC('Sagar', 'Sangamwadi')
#
# print(obj.show())
# print(getattr(obj, 'name'))
# setattr(obj, 'name', "Rahul")
# print(obj.name)
#
# print(obj.__doc__)
# print(obj.__module__)
# print(__name__)

obj2 = xyz('rahul', 'Pashan', 'Pune', 'Veritas')
print(dir(obj2))
print(obj2._xyz__number)
print("ABC display :", obj2._ABC__dispay())
print(obj2.display_class(34567))
print(obj2.display())
print(obj2.show())
print(obj2.get_prime_number(20))


# a = 20
# b = 30
#
# aa = 'a'
# bb = 'b'
# result1 = int.__add__(a, b)
# print(result1)
# result2 = str.__add__(aa, bb)
# print(result2)

class Home:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise("Please provide valid price")

    @price.deleter
    def price(self):
        del self._price
        

obj = Home(3456)

print(obj.price)

obj.price = 2345

print(obj.price)


"""

