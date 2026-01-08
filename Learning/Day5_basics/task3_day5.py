
from datetime import date

with open("practice.txt", "w") as file:
     file.write("\n Test case passed ")

with open("practice.txt", "a") as file:
    today = date.today()
    file.write("\n" + str(today))

