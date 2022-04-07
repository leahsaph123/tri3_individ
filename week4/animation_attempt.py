import time

ANSI_HOME_CURSOR = u"\033[1;1f"
YELLOW_GROUND = "\u001b[33m"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# base only prints the "blue line", not necessary for ship to move
def base():
  print(ANSI_HOME_CURSOR)
  print("\n\n\n\n\n\n\n")
  print(OCEAN_COLOR + "  " * 35)
  print(RESET_COLOR)


def obstacle(position):
  spaces = " " * position
  print(ANSI_HOME_CURSOR)
  print("\n\n\n")
  print(spaces + "    |\   ")
  print(spaces + "    |/   ")
  #print(end="")
  print(spaces + "\__ |__/ ")
  print(spaces + " \____/  ")

def move_obstacle():
  start = 0
  end = 60
  step = 2

  base()
  
  for position in range(start, end, step):
    obstacle(position)
    time.sleep(.1)

move_obstacle()

def character():
  print(ANSI_HOME_CURSOR)
  print("\n\n\n")
  print(" O ")
  print("/|\ ")
  print(" | ")
  print(r"/ \ ")
        
character()