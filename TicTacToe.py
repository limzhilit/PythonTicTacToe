from PlayGame import *

while True:
# representing board
  print("Welcome to TicTacToe")
  play = input("New Game? (y/n) ")
  if play == 'n':
    break
  board = [" " for _ in range(9)]
  mode = 0
  while True:
    try:
      mode = int(input("1: PvP \n2: Computer\n"))
      if mode < 1 or mode > 2:
        print("Invalid input. Please enter 1 or 2.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter 1 or 2.")
  if mode == 2:
    while True:
      try:
        temp = int(input("1: Easy \n2: Hard\n"))
        if temp == 2:
          mode = 3
        if temp < 1 or temp > 2:
          print("Invalid input. Please enter 1 or 2.")
          continue
        break
      except ValueError:
        print("Invalid input. Please enter 1 or 2.")
  play_game(board, mode)
