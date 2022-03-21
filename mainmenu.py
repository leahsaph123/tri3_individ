import fibonacci
import menus
import treedraw
import listsandloops
import ship

# Menu options as a dictionary
menu_options = {
    1: 'submenu',
    2: 'treedraw',
    3: 'fibonacci',
    4: 'lists and loops',
    5: 'ship',
    6: 'exit'
}


# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    #runOptions()


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


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            print("1: submenu")
            print("2: treedraw")
            print("3: fibonacci")
            print("4: lists and loops")
            print("5: exit")
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                submenu()
            elif option == 2:
                tree()
            elif option == 3:
                fibo()
            elif option == 4:
                landl()
            # Exit menu
            elif option == 5:
                shipp()
            # Exit menu
            elif option == 6:
                print('Exiting! Thank you! Good Bye...')
                print('Exciting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    runOptions()