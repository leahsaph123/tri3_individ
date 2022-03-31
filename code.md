{% include jekyllnav.html %}

# Week 3 Code

<p> For Week 3, I added a Tic Tac Toe game to my crossover's repository <p>
  
```
  import random 

     #set up the tic tac toe board
board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
  
  #print the board, make it a function so that you can call it
def make_board(board):
      print(board[1] + ' | ' + board[2] + ' | ' + board[3])
      print("---------")
      print(board[4] + ' | ' + board[5] + ' | ' + board[6])
      print("---------")
      print(board[7] + ' | ' + board[8] + ' | ' + board[9])

move = "player"

  # get player move
def player_next_move(board, move):
      position = input("Please input your next move: ")
      position = int(position)
  
      while (position < 1 or position > 9 or board[position] == 'X' or board[position] == 'O'):
          position = input("Please input your next move between 1 and 9 or in an empty space: ")
          position = int(position)
  
      board[position] = 'X'
      make_board(board)
      move = "computer"
  
# get computer move
def computer_next_move(board, move):
      computer_position = random.randint(1,9)
      while (computer_position < 1 or computer_position > 9 or board[computer_position] == 'X' or board[computer_position] == 'O'):
          computer_position = random.randint(1,9)
  
      board[computer_position] = 'O'
  
      make_board(board)
      move = "player"
  
 # check if either computer or player won
def check_if_won(board):
  
      position_1 = board[1]
      position_2 = board[2]
      position_3 = board[3]
      position_4 = board[4]
      position_5 = board[5]
      position_6 = board[6]
      position_7 = board[7]
      position_8 = board[8]
      position_9 = board[9]
  
      if (position_1 == position_2 == position_3 == 'X') or (position_4 == position_5 == position_6 == 'X') or (position_7 == position_8 == position_9 == 'X') or (position_1 == position_4 == position_7 == 'X') or (position_2 == position_5 == position_8 == 'X') or (position_3 == position_6 == position_9 == 'X') or (position_1 == position_5 == position_9 == 'X') or (position_3 == position_5 == position_7 == 'X'):
          print("you win!")
          return True
      elif (position_1 == position_2 == position_3 == 'O') or (position_4 == position_5 == position_6 == 'O') or (position_7 == position_8 == position_9 == 'O') or (position_1 == position_4 == position_7 == 'O') or (position_2 == position_5 == position_8 == 'O') or (position_3 == position_6 == position_9 == 'O') or (position_1 == position_5 == position_9 == 'O') or (position_3 == position_5 == position_7 == 'O'):
          print("computer wins :(")
          return True
      else:
          return False

win = False

def end_game(win, move):
  for number_of_moves in range(9):
    if (win == True):
        break
    if (number_of_moves == 8 and win == False):
          print("tie")
          break
    if (move == "player"):
      player_next_move(board, move)
      move = "computer"
      win = check_if_won(board)
      if win == False:
        print("where you moved ^")
        print("-------------")
        print("-------------")
        print("where computer moved v")
    elif (move == "computer"):
      computer_next_move(board, move)
      move = "player"
      win = check_if_won(board)
    
    
if __name__ == "__main__":
  make_board(board)
  end_game(win, move)
 ```

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@leahbogomolny/tri3individ?lite=true"></iframe>
