with open("items.txt", "r") as file:
    for line in file:
        item = line.strip()
        if item:
            print(f"Processing {item}")
