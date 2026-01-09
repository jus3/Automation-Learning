
""" r=read, w=write, a=append, r+=read+write """

# # To Read a file
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# #TO Read line by line
# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())
#
# #To Write a file
# with open("output.txt", "w") as file:
#     file.write("Test execution started")
#
# #Append to a file
# with open("output.txt", "a") as file:
#     file.write("\nTest case passed")
#
# #Exception Handling
# try:
#     with open("missing.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
#
# #Working with Structured Files
# with open("users.txt", "r") as file:
#     for line in file:
#         name, email = line.strip().split(",")
#         print(name, email)
#
# #Built-in Modules
# import os
# import sys
# import datetime
#
#
# from testcase import log_message
# log_message("Test completed")

from logger import log_result

try:
    with open("testcase.txt", "r") as file:
        for line in file:
            test_name = line.strip()

            if test_name:
                print(f"Executing {test_name}")
                log_result(test_name, "PASSED")

except FileNotFoundError:
    print("ERROR: testcase.txt not found")


