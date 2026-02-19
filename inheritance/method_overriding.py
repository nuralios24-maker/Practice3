class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()

class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet() 
        print("I am a student.")

s = Student()
s.greet()



class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

sq = Square(5)
print(sq.area())

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def skills(self):
        print("Driving and Cooking")

ch = Child()
ch.skills()
