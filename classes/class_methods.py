class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        return cls(name, int(age))

p = Person.from_string("Ali,25")
print(p.name, p.age)

class Employee:
    raise_amount = 1.05

    def __init__(self, salary):
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count

u1 = User("Ali")
u2 = User("Sara")

print(User.total_users())

class Car:
    max_speed = 200

    @classmethod
    def is_speed_allowed(cls, speed):
        return speed <= cls.max_speed

print(Car.is_speed_allowed(180))  # True
print(Car.is_speed_allowed(250))  # False

class Shape:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_circle(cls):
        return cls("Circle")

    @classmethod
    def create_square(cls):
        return cls("Square")

c = Shape.create_circle()
s = Shape.create_square()

print(c.name)  # Circle
print(s.name)  # Square

