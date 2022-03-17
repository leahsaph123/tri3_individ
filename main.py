# import "packages" from flask
from flask import Flask, render_template,request
import requests
import json
import random
import math

import listsandloops
import menus
import treedraw
import fibonacci

main_menu_options = {
    1: "menus",
    2: "tree",
    3: "fibonacci",
    4: "lists and loops"
}

def print_main_menu():
    for key in main_menu_options.keys():
        print(key, '--', main_menu_options[key])
    runOpt()

def men():
    menus.print_menu2()

def tree():
    treedraw.drawTree()

def fib():
    fibonacci.fibonacci()

def landl():
    listsandloops.run_loops()


def runOpt():
    while True:
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                men()
            elif option == 2:
                tree()
            elif option == 3:
                fib()
            elif option == 4:
                landl()
            elif option == 5:
                print("That's all!")
                exit()
            else:
                print("Invalid option. choose a number between 1 and 4")
        except ValueError:
            print("Invalid input. Please enter and integer")


# create a Flask instance
from __init__ import app

if __name__ == "__main__":
    print_main_menu()
    app.run(debug=True, port="5002")