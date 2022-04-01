{% include jekyllnav.html %}

### Week 1
For week 1 I made a program that prints out a fibonacci sequence and a program that prints out a list using a for loop, while loop, or a recursive loop.
For Fibonacci:
```
def fiboooo():
    n = int(input("number of terms? "))
    while (n <= 2 or n > 50):
        n = int(input("please provide a valid input: "))

    def fibonacci(number):
        if number <= 1:
            return number
        else:
            return(fibonacci(number - 1) + fibonacci(number - 2))

    for index in range(n):
        if index == range(n):
            print(fibonacci(index), end="")
        else:
            print(fibonacci(index), end=", ")
```

For lists:
```
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
```
<iframe frameborder="0" width="100%" height="1000px" src="https://replit.com/@leahbogomolny/tri3_individ?lite=true"></iframe>
