import random

fruits_to_guess = ["strawberry", "banana", "apple", "mango", "watermelon"]

animals_to_guess = ["dog", "cat", "horse", "sheep", "bunny"]
  
def guessing_game():
  print("---------")
  print("Guessing Game")
  print("---------")
  print("Options: ")
  print("1: fruits")
  print("2: animals")
  subject_choice = str(input("please choose a subject by inputting 1 or 2: "))
    
  while not (subject_choice == "1" or subject_choice == "2"):
    subject_choice = input("please input a valid number: ")
  
  if subject_choice == "1":
    word_to_guess = random.choice(fruits_to_guess)
  else:
    word_to_guess = random.choice(animals_to_guess)
  
  guess = input("what is your guess? ")
  if guess == word_to_guess:
    print("congrats! you guessed the right word!")
  else:
    print("your guess was incorrect :(")
    print("the correct guess was:", word_to_guess)
  

#guessing_game()

# keep_playing = input("would you like to play again? y/n ")
# while keep_playing == "y":
#   guessing_game()
#   keep_playing = input("would you like to play again? y/n ")
