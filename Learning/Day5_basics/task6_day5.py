with open("items.txt", "r") as file:
    for line in file:
        item = line.strip()

        if not item:
            continue

        if "fail" in item.lower():
            result = "FAILED"
        else:
            result = "PASSED"

        with open("results.txt", "a") as out:
            out.write(f"{item} : {result}\n")
