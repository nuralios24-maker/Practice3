class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()


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

class Mother:
    def cooking(self):
        print("Cooking skills")

class Father:
    def driving(self):
        print("Driving skills")

class Child(Mother, Father):
    def play(self):
        print("Playing skills")

c = Child()
c.cooking()
c.driving()
c.play()

class Father:
    def __init__(self):
        print("Father initialized")

class Mother:
    def __init__(self):
        print("Mother initialized")

class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child initialized")

c = Child()

