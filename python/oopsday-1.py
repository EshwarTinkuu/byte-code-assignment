# 1.create a class
class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Price:", self.price)


car1 = Car("BMW", "Black", 5000000)
car2 = Car("Audi", "White", 4000000)

car1.display()
car2.display()


# 2.create a mobile class
class Mobile:
    def __init__(self, name, price, ram):
        self.name = name
        self.price = price
        self.ram = ram

    def display(self):
        print("Mobile:", self.name)
        print("Price:", self.price)
        print("RAM:", self.ram)


m1 = Mobile("Samsung", 25000, "8GB")
m2 = Mobile("iPhone", 60000, "8GB")

m1.display()
m2.display()

# 3. Create an Employee class
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Salary:", self.salary)


e1 = Employee("Eshwar", 101, 25000)
e2 = Employee("Rahul", 102, 30000)

e1.display()
e2.display()

# 5. Create a BankAccount class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


b1 = BankAccount("Eshwar", 10000)
b2 = BankAccount("Rahul", 20000)

b1.display()
b2.display()

# Create a Product class

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 10)

p1.display()
p2.display()