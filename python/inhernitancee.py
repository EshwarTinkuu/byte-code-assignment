class Parent:
    def display(self):
        print("This is parent class")

class Child(Parent):
    pass

obj = Child()
obj.display()

# Single Inheritance
class Father:
    def house(self):
        print("Father has a house")

class Son(Father):
    def bike(self):
        print("Son has a bike")

obj = Son()
obj.house()
obj.bike()

# Multiple Inheritance
class Father:
    def father_name(self):
        print("Father: Ramesh")

class Mother:
    def mother_name(self):
        print("Mother: Sita")

class Child(Father, Mother):
    def child_name(self):
        print("Child: Rahul")

obj = Child()
obj.father_name()
obj.mother_name()
obj.child_name()

# Multilevel Inheritance
class Grandfather:
    def house(self):
        print("Grandfather has a house")

class Father(Grandfather):
    def car(self):
        print("Father has a car")

class Son(Father):
    def bike(self):
        print("Son has a bike")

obj = Son()
obj.house()
obj.car()
obj.bike()
# Hierarchical Inheritance

class Father:
    def property(self):
        print("Father has property")

class Son(Father):
    def bike(self):
        print("Son has a bike")

class Daughter(Father):
    def car(self):
        print("Daughter has a car")

obj1 = Son()
obj1.property()
obj1.bike()

obj2 = Daughter()
obj2.property()
obj2.car()