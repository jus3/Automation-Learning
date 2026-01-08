def write_message(msg):
    with open("messages.txt", "a") as file:
        file.write(msg + "\n")
