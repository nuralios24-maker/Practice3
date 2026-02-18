class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Pet("Cat", 4)
pet2 = Pet("Dog", 10)

print("Name:", pet1.name, "|", pet1.age, "year")
print("Name:", pet2.name, "|", pet2.age, "year")
print("Name:", pet2.name, "|", pet1.age, "year")
print("Name:", pet1.name, "|", pet2.age, "year")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)