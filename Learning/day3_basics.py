# def greet_user(name):
#     print(f"Hello, {name}")
#
# greet_user("Het")
#
#
# def add(a, b):
#     return a + b
#
# result = add(2, 3)
# print(result)
#
#
# ages = [55, 30, 35]
#
# def age_status(age):
#     if age > 30:
#         return "Bad"
#     elif age < 30:
#         return "Good"
#     else:
#         return "Best"
# for age in ages:
#     print(f"{age}: {age_status(age)}")
#
#
# def get_age_status():
#     try:
#         age = int(input("Enter age: "))
#         return age_status(age)
#     except ValueError:
#         return "Invalid age input"
#
# print(get_age_status())
#
from configparser import MAX_INTERPOLATION_DEPTH


#OWN TASK
#
# def age_status(age):
#     if age > 30:
#         return "Bad"
#     elif age < 30:
#         return "Good"
#     else:
#         return "Best"
#
#
# def read_age():
#     try:
#         age = int(input("Enter your age: "))
#         return age
#     except ValueError:
#         return None
#
# #Main Execution
#
# ages = []
#
# for i in range(4):
#     age = read_age()
#
#     if age is None:
#         print("Invalid Data")
#         #ages.append(0)  #Removing this line it will store age as default 0
#     elif age < 0:
#         print("Skipped invalid age")
#     elif age >= 60:
#         print(f"{age}: Senior")
#     else:
#         print(f"{age}: {age_status(age)}")
#


#TASK Calculator

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def read_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

#Main Execution

num1 = read_number("Enter a number: ")
num2 = read_number("Enter another number: ")

if num1 is None or num2 is None:
    print("Invalid Input, Please enter numbers")
else:
    print(f"Addition: {add(num1,num2)}")
    print(f"Subtraction: {subtract(num1,num2)}")
    print(f"Multiplication: {multiply(num1,num2)}")
    print(f"Division: {divide(num1,num2)}")

