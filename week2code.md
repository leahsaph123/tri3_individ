{% include jekyllnav.html %}

### Week 2
During week 2 I learned how to use Python classes. I made a program that runs the "!" function on a given number, one that finds the derivative of a function, and another one that checks if a word is a palindrome

For the factorial function:
```
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
```

For the derivative function: 
```
def derivative():
    degree = 4
    coefficient = 3
    print("the equation was: 3x^4 + 10")
    print("your derivative is: ", coefficient * degree, "x^", degree - 1)


class Derivative:
    def __call__(self):
        degree = 3
        coefficient = 2
        print("the equation was: 2x^3 + 5")
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
```

For the palindrome function:
```
class Palindrome:

    def __call__(self, inputted_word):
        # get user input

        # sets characters that aren't allowed
        nope = "1234567890!@#$%^&*()-_=+;:'<,>.?/"
        space_nope = " "

        # iterate through non letters to remove from word
        for character in nope:
            inputted_word = inputted_word.replace(character, "")
            # inputted_word1 = inputted_word1.replace(character, "")
            # inputted_word2 = inputted_word2.replace(character, "")

        actual_word = inputted_word
        # actual_word1 = inputted_word1
        # actual_word2 = inputted_word2

        # separates space from rest of the word in order to be able to read the word when it's reprinted
        for character in space_nope:
            inputted_word = inputted_word.replace(character, "")
            # inputted_word1 = inputted_word1.replace(character, "")
            # inputted_word2 = inputted_word2.replace(character, "")

        # splits word in half so we can compare it to itself
        length = int(len(inputted_word) / 2)

        # allows to check where we are in the word
        index_front = 0
        index_back = len(inputted_word) - 1

        # allows to check if word passed the check
        check = 0
        # index of where word failed the check
        error = 0

        # iterate through the word to check if it's a palindrome
        for index in range(0, length):
            # gets specific index of the word
            first = inputted_word[index_front]
            last = inputted_word[index_back]
            if first.lower() == last.lower():
                index_front = index_front + 1;
                index_back = index_back - 1;
                check = check + 1;
            else:
                error = index
                break

        # checks if all letters in the word passed the check
        if check == length:
            print("congrats! the word '", actual_word, "' is a palindrome")
        else:
            print("your word '", actual_word, "' is not a palindrome")
            # prints the location of failure
            print("the word failed on the letter '", inputted_word[error], "' at index", error)


checksif = Palindrome() # object instantiation and run __init__ method
```
<iframe frameborder="0" width="100%" height="1000px" src="https://replit.com/@leahbogomolny/tri3individ?lite=true"></iframe>
