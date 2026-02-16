"""
class Employee:
    def __init__(self, id, name, salary, designation):
        self.id = id
        self.name = name
        self.salary = salary
        self.designation = designation

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")

emp1 = Employee(100, 'sam', 10000, 'head')
print(emp1.name)
"""
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, second):
        left = self.x + second.x
        right = self.y + second.y
        return Complex(left, right) 
    def __repr__(self):
        return str(self.x) + ' + i' + str(self.y) 

inp1 = Complex(1, 2)
inp2 = Complex(3, 4)
print(inp1 + inp2)