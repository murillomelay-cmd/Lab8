# Step 1: Define a class named Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Step 2: Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Step 3: Print the car details using the method
print(my_car.display_info())

# Step 1: Define a class with private attributes
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"New balance: ${self.__balance}"

    def get_balance(self):
        return f"Balance: ${self.__balance}"

# Step 2: Create an object and test encapsulation
account = BankAccount("Alice", 5000)

# Step 3: Deposit money and display the updated balance
print(account.deposit(1500))
print(account.get_balance())

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}."

# Subclass
class Student(Person):
    def introduce(self):
        return f"Hi, I'm {self.name}, and I'm a student."

# Objects using "Melanie"
person = Person("Melanie")
student = Student("Melanie")

print(person.introduce())
print(student.introduce())

# Step 1: Define a base class
class Shape:
    def area(self):
        return "Calculating area..."

# Step 2: Define subclasses with their implementations
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Step 3: Create objects and call their methods
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")

# Step 1: Import the datetime module
import datetime
# Step 2: Create an object for the current date and time
current_time = datetime.datetime.now()
# Step 3: Print the formatted date and time
print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
# Step 1: Define a class with a static method
class MathOperations:
    @staticmethod
    def square(num):
        return num * num

# Step 2: Get user input
user_input = int(input("Enter a number to square: "))

# Step 3: Call the static method with user input
result = MathOperations.square(user_input)

# Step 4: Print the result
print("Square of", user_input, ":", result)
# Step 1: Define a class with overloaded operators
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

# Step 2: Create account objects and add their balances
account1 = BankAccount(5000)
account2 = BankAccount(3000)

total_balance = account1 + account2  # Combines the balances

# Step 3: Print the result
print(f"Total Balance: P{total_balance.balance}")
from abc import ABC, abstractmethod

# Step 1: Define an abstract class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# Step 2: Define a subclass implementing the abstract method
class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing machine is now running."

# Step 3: Create an object of the subclass and call the method
wm = WashingMachine()
print(wm.turn_on())

# Step 1: Define multiple classes
class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass  # Inherits show() based on MRO

# Step 2: Create an object of class D and call the method
obj = D()
print(obj.show())  # Output depends on MRO