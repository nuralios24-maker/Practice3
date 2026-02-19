
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ali", 5)
print(s.name, s.grade)

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

ch = Child()
ch.skills()
