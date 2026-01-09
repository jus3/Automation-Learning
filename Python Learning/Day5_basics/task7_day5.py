while True:
    print("\n 1. Add Task")
    print("\n2. view Task")
    print("\n3. Exit")

    choice = input("Choose an option: ")


    if choice == "3":
        print("Exiting...")
        break

    elif choice == "2":
        try:
            with open("todo.txt", "r") as file:
                print("\nYour tasks:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No tasks found")

    elif choice == "1":
        task = input("Enter task: ")

        with open("todo.txt", "a") as file:
            file.write(task + "\n")

        print("Task added")

    else:
        print("Invalid option")



