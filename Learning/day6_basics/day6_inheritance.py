class User:# Superclass (Parent Class)
    def __init__(self, username):
        self.username = username  # Instance variable

    def display_user(self):
        print(f"User: {self.username}")# Method of the superclass


class Student(User): # Subclass (Child Class)
    def __init__(self, username, marks):
        super().__init__(username)  # super() calls the constructor of the superclass (User)

        self.marks = marks # Instance variable

    def display_student(self):
        print(f"Marks: {self.marks}") # Method of the subclass


s1 = Student(username="Het", marks=70) # Object
s2 = Student(username="Rajdeep", marks=80) # Object



s1.display_user() # Superclass Method calls
s1.display_student() # subclass Method calls


s2.display_user()  # Superclass Method calls
s2.display_student() # subclass Method calls
