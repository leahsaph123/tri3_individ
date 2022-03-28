class Factorial:
    def __init__(self):
        self.factseq = []

    def __call__(self):
        num = int(input("Enter a number: "))
        while num < 0:
            num = int(input("please enter a positive number: "))
        while num == 0:
            print("the factorial of 0 is 1")
            num = int(input("please enter another number: "))

        def recur_factorial(num):
            if num == 1:
                return num
            else:
                return num*recur_factorial(num-1)
        list_of_terms = [num]

        for index in range(num - 1):
            list_of_terms.append(num - index - 1)

        print(num, "factorial is ", list_of_terms)

        print("The factorial of", num, "is", recur_factorial(num))


fact_of = Factorial()  # object instantiation and run __init__ method
#fact_of() # object running __call__ method

