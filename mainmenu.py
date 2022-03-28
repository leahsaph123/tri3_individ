from week0 import menus, ship, treedraw
from week1 import fibonacci, listsandloops
from week2 import palindrome, factorial

# Menu options as a dictionary
menuu_options = {
    0: 'week 0',
    1: 'week 1',
    2: 'week 2',
    3: 'week 3',
    10: 'exit'
}

# Print menu options from dictionary key/value pair
def print_menu():
    for key in menuu_options.keys():
        print(key, '--', menuu_options[key] )
    #runOptions()


week0_options = {
    1: 'submenu',
    2: 'treedraw',
    3: 'ship'
}

# print statement for each week
def print_week0():
    while True:
        try:
            print("\n1: submenu")
            print("2: treedraw")
            print("3: ship")
            print("4: back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                submenu()
            elif option == 2:
                tree()
            elif option == 3:
                shipp()
            elif option == 4:
                break
            # Exit menu
            elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

week1_options = {
    1: 'fibonacci',
    2: 'lists and loops'
}

def print_week1():
    while True:
        try:
            print("\n1: fibonacci")
            print("2: lists and loops")
            print("3: back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                fibo()
            elif option == 2:
                landl()
            elif option == 3:
                break
            # Exit menu
            elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


week2_options = {
    1: 'factorial',
    2: 'palindrome',
}

def print_week2():
    while True:
        try:
            print("\n1: factorial")
            print("2: palindrome")
            print("4: back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                factorial.fact_of()
            elif option == 2:
                palindrome.checksif()
            elif option == 4:
                break
            # Exit menu
            elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


# menu option 1
def submenu():
    menus.print_menu2()


# menu option 2
def tree():
    treedraw.drawTree()


# menu option 3
def fibo():
    fibonacci.fiboooo()


def landl():
    listsandloops.run_loops()

def shipp():
    ship.ship()

def palii():
    palindrome.palindrome()


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            print("\n0: week 0")
            print("1: week 1")
            print("2: week 2")
            print("3: week 3")
            print("10: exit")
            option = int(input('Enter your choice: '))
            if option == 0:
                print_week0()
            elif option == 1:
                print_week1()
            elif option == 2:
                print_week2()
            # Exit menu
            elif option == 10:
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    runOptions()