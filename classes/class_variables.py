class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

u1 = User("Ali")
u2 = User("Sara")

print(User.count)

class Product:
    tax_rate = 0.2

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price * (1 + Product.tax_rate)

p = Product(100)
print(p.final_price())

class Website:
    default_language = "English"

    def __init__(self, name):
        self.name = name

site1 = Website("Shop")
site2 = Website("Blog")

print(site1.default_language)
print(site2.default_language)

class Student:
    students_list = []

    def __init__(self, name):
        self.name = name
        Student.students_list.append(name)

s1 = Student("Ali")
s2 = Student("Amina")

print(Student.students_list)

class Car:
    max_cars = 3
    created_cars = 0

    def __init__(self, model):
        if Car.created_cars >= Car.max_cars:
            print("Don't creat new a car")
        else:
            self.model = model
            Car.created_cars += 1

c1 = Car("BMW")
c2 = Car("Audi")
c3 = Car("Toyota")
c4 = Car("Honda")
