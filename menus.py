"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Red',
    2: 'Green',
    3: 'Blue',
    4: 'Purple',
    5: 'Exit'
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def red():
    red_menu_options = {
        1: '7',
        2: '3',
        3: '9',
        4: '1'
    }
    def print_menu_red():
        for key in red_menu_options.keys():
            print(key, '--', red_menu_options[key] )
    print_menu_red()
    red_menu_submenu()

def red_menu_submenu():
    while True:
        try:
            option = int(input('Enter your choice 1-4 '))
            if option == 1:
                print('something good will happen to you tomorrow')
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            elif option == 2:
                print('you will die eventually')
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            elif option == 3:
                print('you will be rich')
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            elif option == 4:
                print('you will do well on something')
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            elif option == 5:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')




# menu option 2
def green():
    red_menu_options = {
        1: '7',
        2: '3',
        3: '9',
        4: '1'
    }
    def print_menu_red():
        for key in red_menu_options.keys():
            print(key, '--', red_menu_options[key] )
    print_menu_red()
    red_menu_submenu()

# menu option 3
def blue():
    red_menu_options = {
        1: '7',
        2: '3',
        3: '9',
        4: '1'
    }
    def print_menu_red():
        for key in red_menu_options.keys():
            print(key, '--', red_menu_options[key] )
    print_menu_red()
    red_menu_submenu()

def purple():
    red_menu_options = {
        1: '7',
        2: '3',
        3: '9',
        4: '1'
    }
    def print_menu_red():
        for key in red_menu_options.keys():
            print(key, '--', red_menu_options[key] )
    print_menu_red()
    red_menu_submenu()

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                red()
            elif option == 2:
                green()
            elif option == 3:
                blue()
            elif option == 4:
                purple()
            # Exit menu
            elif option == 5:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__=='__main__':
    # print_menu1()
    print_menu2()