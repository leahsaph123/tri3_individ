def derivative():
    degree = 4
    coefficient = 3
    print("your derivative is: ", coefficient * degree, "x^", degree - 1)


class Derivative:
    def __call__(self):
        degree = 3
        coefficient = 2
        print("your derivative is: ", coefficient * degree, "x^", degree - 1)


derivative_of = Derivative()


def runfun():

    method = input("would you like to run the oop or imperative in order to find a derivative? ")

    while not (method == "oop" or method == "imperative"):
        method = input("please input either 'oop' or 'imperative': ")

    if method == "oop":
        derivative_of()
    else:
        derivative()

