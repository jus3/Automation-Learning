"""
What is a Class? (Plain English)

A class is a blueprint.
An object is a real thing created from that blueprint.
"""

class Student:
    pass

"""Creating an Object"""

s1 = Student()
print(s1)

# Student → class
#
# s1 → object


# ----------------------------------------------------------------------------------------


"""
What __init__ does (Constructor)

Runs automatically when object is created
"""
# Student with data
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Het", "A")
print(s1.name)
print(s1.grade)

# self = current object
#
# self.name = object variable

# ----------------------------------------------------------------------------------------
"""
Methods (Object Behavior)

Methods = functions inside a class
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

s1 = Student("Het", "A")
s1.display()

# ----------------------------------------------------------------------------------------

"""
Using OOP:

Page Objects
Test Classes
Utilities
Clean separation
"""

class LoginTest:
    def execute(self):
        pass