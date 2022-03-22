
def fiboooo():
    n = int(input("number of terms? "))
    while (n < 0 or n > 50):
        n = int(input("please provide a valid input: "))

    def fibonacci(number):
        if number <= 1:
            return number
        else:
            return(fibonacci(number - 1) + fibonacci(number - 2))

    for index in range(n):
        print(fibonacci(index))
#fiboooo()