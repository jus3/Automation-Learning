# #basic
# for i in range(3):
#     print(i)
#
#
# # Project Oriented
# devices = ["hi", "hello", "hey"]
#
# for device in devices:
#     print(f"Validating device: {device}")
#     if device == "hi": print("Apple device")
#     elif device == "hello": print("Android device")
#     elif device == "hey": print("Blackberry device")
#     else:
#         print("Unknown device")
#from Python Learning.day1_basics import age

# response = 3
#
# while response <= 3:
#     print(f"Attempt {response}")
#     response += 1

# This will break and show error
# for i in range(100):
#     if i == 110:
#         break
#     print(i)

#this will skip 1 in output and continue Execution till end
# for i in range(5):
#     if i == 1:
#         continue
#     print(i)


#Loop + condition
# ages = [2.5, 3.1, 301]
#
# for age in ages:
#     if age > 30:
#         print(f"{age}: Bad")
#     elif age < 30:
#         print(f"{age}: Good")
#     else:
#         print(f"{age}: Best")


#OWN TASK
ages = [29,35,40]

for age in ages:
    if age > 30:
        print(f"{age}: Bad")
    elif age == 30:
        print(f"{age}: Best")
    else:
        print(f"{age}: Good")

response = 29

while response <= 29:
    print(f"{response}: This is correct")
    response += 1


#Task

secret_number = 3
attempts = 0

while True:
    guess = int(input("Enter a number (1-100) : "))
    attempts += 1

    if guess == secret_number:
        print("Good job, you guessed the number")
        break
    elif guess > secret_number:
        print("You guessed too high")
    elif guess < secret_number:
        print("You guessed too low")
    else:
            print("Wrong Guess")














