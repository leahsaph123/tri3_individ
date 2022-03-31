{% include jekyllnav.html %}

# Week 3 Code

#### For Week 3, I added a Tic Tac Toe game to my crossover's repository
  
```
  import random 

class colors:  
  tie = '\033[94m'
  ooo = '\033[99m'
  win = '\033[92m'
  lose = '\33[31m'
  normal = '\033[0m'

     #set up the tic tac toe board
board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
X = colors.tie + 'X' + colors.normal
O = colors.tie + 'X' + colors.normal
  
  #print the board, make it a function so that you can call it
def make_board(board):
      print(board[1] + ' | ' + board[2] + ' | ' + board[3])
      print("---------")
      print(board[4] + ' | ' + board[5] + ' | ' + board[6])
      print("---------")
      print(board[7] + ' | ' + board[8] + ' | ' + board[9])

move = "player"

  # get player move
def player_next_move(board, move, X, O):
      position = input("Please input your next move: ")
      position = int(position)
  
      while (position < 1 or position > 9 or board[position] == X or board[position] == O):
          position = input("Please input your next move between 1 and 9 or in an empty space: ")
          position = int(position)
  
      board[position] = colors.tie + 'X' + colors.normal
      make_board(board)
      move = "computer"
  
# get computer move
def computer_next_move(board, move, X, O):
      computer_position = random.randint(1,9)
      while (computer_position < 1 or computer_position > 9 or board[computer_position] == X or board[computer_position] == O):
          computer_position = random.randint(1,9)
  
      board[computer_position] = colors.tie + 'O' + colors.normal
  
      make_board(board)
      move = "player"
  
 # check if either computer or player won
def check_if_won(board, X, O):
  
      position_1 = board[1]
      position_2 = board[2]
      position_3 = board[3]
      position_4 = board[4]
      position_5 = board[5]
      position_6 = board[6]
      position_7 = board[7]
      position_8 = board[8]
      position_9 = board[9]

      
  
      if (position_1 == position_2 == position_3 == X) or (position_4 == position_5 == position_6 == X) or (position_7 == position_8 == position_9 == X) or (position_1 == position_4 == position_7 == X) or (position_2 == position_5 == position_8 == X) or (position_3 == position_6 == position_9 == X) or (position_1 == position_5 == position_9 == X) or (position_3 == position_5 == position_7 == X):
          print(colors.win + "you win!" + colors.normal)
          return True
      elif (position_1 == position_2 == position_3 == O) or (position_4 == position_5 == position_6 == O) or (position_7 == position_8 == position_9 == O) or (position_1 == position_4 == position_7 == O) or (position_2 == position_5 == position_8 == O) or (position_3 == position_6 == position_9 == O) or (position_1 == position_5 == position_9 == O) or (position_3 == position_5 == position_7 == O):
          print(colors.lose + "computer wins :(" + colors.normal)
          return True
      else:
          return False

win = False

def end_game(win, move, X, O):
  for number_of_moves in range(9):
    if (win == True):
        break
    if (number_of_moves == 8 and win == False):
          print("tie")
          break
    if (move == "player"):
      player_next_move(board, move, X, O)
      move = "computer"
      win = check_if_won(board, X, O)
      if win == False:
        print("where you moved ^")
        print("-------------")
        print("-------------")
        print("where computer moved v")
    elif (move == "computer"):
      computer_next_move(board, move, X, O)
      move = "player"
      win = check_if_won(board, X, O)
    
    
if __name__ == "__main__":
  make_board(board)
  end_game(win, move, X, O)
 ```
#### I also created a palindrome file

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
           

        actual_word = inputted_word
      

        # separates space from rest of the word in order to be able to read the word when it's reprinted
        for character in space_nope:
            inputted_word = inputted_word.replace(character, "")
            

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

#### I made a second tree program as well
```
def drawTree():
    height = input("how tall would you like your tree? ")
    while not (height.isdigit()):
        height = input("please provide a number: ")

    height = int(height)
    k = height

    # outer loop to handle number of rows
    for i in range(0, height):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            # printing stars
            print("# ", end="")
        # ending line after each row
        print("\r")

    spaces = round(height / 2)
    print_spaces = " " * height
    print(print_spaces + "#" + print_spaces)
    print(print_spaces + "#" + print_spaces)
```

#### Finally, I added all of this code into a week 3 submenu of the main menu
```
def print_week3():
  while True:
        try:
            print("\n1: tree")
            print("2: palindrome")
            print("3: tictactoe")
            print("4: back to main menu")
            option = int(input('Enter your choice: '))
            if option == 1:
                tree2.drawTree()
            if option == 2:
                palindrome.checksif(inputted_word="A man, a plan, a canal -- Panama!")
                palindrome.checksif(inputted_word="racecar")
                palindrome.checksif(inputted_word="r2acecar")
                palindrome.checksif(inputted_word="raaceac")
            elif option == 3:
              board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
              move = "player"
              win = False
              right.make_board(board)
              right.end_game(win, move)
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
```
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@leahbogomolny/tri3individ?lite=true"></iframe>
