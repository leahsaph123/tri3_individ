# empty list
list = []

# adding to list
list.append({
        "name": "Leah",
        "grade": "12",
        "group mates": ["Jessie", "Allie", "Michael"]
    })

list.append({
    "name": "Jessie",
    "grade": "12",
    "group mates": ["Leah", "Allie", "Michael"]
})

list.append({
    "name": "Allie",
    "grade": "11",
    "group mates": ["Leah", "Jessie", "Michael"]
})

list.append({
    "name": "Michael",
    "grade": "11",
    "group mates": ["Leah", "Jessie", "Allie"]
})

def for_loop():
    for entry in range(len(list)):
        print(list[entry])

def while_loop():
    entry = 0
    while (entry < len(list)):
        print(list[entry])
        entry += 1

def recursive_loop(entry):
    if entry < len(list):
        print(list[entry])
        recursive_loop(entry + 1)
    return

# user chooses which loop to use
def run_loops():
    option = input("would you like to run a for, while, or recursive loop? Please answer with a 'for', 'while', or 'recursive': ")

    while not ((option == "for") or (option == "while") or (option == "recursive")):
        option = input("please give a valid input: ")

    if (option == "for"):
        for_loop()
    elif (option == "while"):
        while_loop()
    elif (option == "recursive"):
        recursive_loop(entry=0)

#run_loops()

