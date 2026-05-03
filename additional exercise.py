class Library:
    def __init__(self):
        self.books = {}

    def borrow(self, title):
        if self.books.get(title) == "available":
            self.books[title] = "borrowed"
            return "Borrowed"
        return "Not available"

lib = Library()
lib.books["Python"] = "available"
print(lib.borrow("Python"))

class Employee:
    def __init__(self, name, rate, hours):
        self.name = name
        self.salary = rate * hours

e = Employee("Alice", 100, 160)
print(e.name, e.salary)

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

c = Cart()
c.add("Laptop")
print(c.items)