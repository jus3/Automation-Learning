# #List
# names = ["Tom", "Jerry", "stuart"]
#
# names.append("QA")
# print(names[2])
#
# #Tuples
# coordinates = (23.0225, 72.5714)
#
# #Dictionaries
# user = {
#     "name": "Jerry",
#     "role": "QA",
#     "experience": 5.6
# }
#
# print(user["name"])
# print(user["role"])
# print(user["experience"])
#
# #Sets
# ids = {101, 102, 103}
# print(ids)
#
# #slicing Mix data
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums[1:4])
# print(nums[::+3])
#
# #List Comprehensions
# x = "2"
# squares = [x*x for x in range(1, 6)]
#
# even = [x for x in range(10) if x % 2 == 0]
#
#
# #Nested Data Structures
#
# employee = {
#     "id": 1,
#     "name": "Het",
#     "skills": ["API", "MQTT", "Manual"],
#     "address": {
#         "city": "Ahmedabad",
#         "country": "India"
#     }
# }
#
# print(employee["address"]["city"])
# print(employee["address"]["country"])


#Task

contacts = {
    "Jerry": {
    "phone": "9999999999",
    "email": "Jerry@test.com"
},
    "Tom": {
    "phone": "8888888888",
    "email": "Tom@test.com"
},
    "Stuart": {
    "phone": "7777777777",
    "email": "Stuart@test.com"
}}

# Fetch contact
print(contacts["Jerry"]["phone"])

# Loop all contacts
for name, details in contacts.items():
    print(name, details["phone"])

