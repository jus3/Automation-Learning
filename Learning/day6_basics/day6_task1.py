class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Student(name="Het", marks=70)
s2 = Student(name="Rajdeep", marks=80)
s3 = Student(name="Harshvi", marks=90)

s1.print_details()
s2.print_details()
s3.print_details()
