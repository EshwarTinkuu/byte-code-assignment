#method overriding
class Father:
    def property(self):
        print("Father has a house")

class Son(Father):
    def property(self):
        print("Son has a car")

obj = Son()
obj.property()

obj=Father()
obj.property()


#
class Father:
    def property(self):
        print("Father has a house")

class Son(Father):
    def property(self):
        super().property()
        print("Son has a car")

obj = Son()
obj.property()
#
class Father:
    def house(self):
        print("Father has a house")

class Son(Father):
    def bike(self):
        print("Son has a bike")

    def show(self):
        super().house()

obj = Son()
obj.show()

#method overloading
class Calculator:

    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = Calculator()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)


class parent:
    def genes(self):
        print("name:" "tinku")

class child(parent):
    def genes(self):
        super().genes()
        print("name:" "child")

obj=child()
obj.genes()

##
class students:
    def __init__(self):
        print("students details")

    def details(self,*args):
        print(args)

obj=students()
obj.details(1,261.50003,"HYD","tinku")
obj.details(1,261.50003,"HYD","tinku",2137632,213312)
obj.details(1,261.50003,"HYD","tinku",23,223,13,13,3,23,3)