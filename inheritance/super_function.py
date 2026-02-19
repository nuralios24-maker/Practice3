class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()

c = Child()
c.greet()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print("Vehicle initialized")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print("Car initialized")

c = Car("Toyota", "Corolla")
print(c.brand, c.model)


class Person:
    def info(self):
        print("I am a person")

class Student(Person):
    def info(self):
        super().info()
        print("I am also a student")

s = Student()
s.info()


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()


class Employee:
    raise_amount = 1.05

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

class Manager(Employee):
    @classmethod
    def set_raise(cls, amount):
        super().set_raise(amount * 2)

Manager.set_raise(0.1)
print(Employee.raise_amount)
print(Manager.raise_amount)

