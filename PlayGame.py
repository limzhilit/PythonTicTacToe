from FunctionToDisplayBoard import print_board
from checkWin import *
from smartComputer import *
import ComputerRandom
import random
from datetime import datetime
from ComputerRandom import *

# play game feature to so user can choose boxes, mark boxes and
# alternate between player moves

# Get current date and time as an integer seed
now = datetime.now()
seed = int(now.strftime("%Y%m%d%H%M%S"))

# Seed the random generator
random.seed(seed)

# function to switch player
def switch_player(current):
  return "o" if current == "x" else "x"

available = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# core method to play a turn
def play_turn(board, current_player, player):
  match player:
    case 1:
      human(board, current_player)
    case 2:
      pcMove(board, current_player, available)
    case 3:
      smart_move(board, current_player)
  return switch_player(current_player)

# human player
def human(board, current_player):
  while True:
  # ask the current player for a position 1–9
    try:
      choice = int(input(f"Player {current_player}, choose a box (1-9): ")) - 1
      if choice < 0 or choice > 8:
        print("Invalid choice. Please enter a number from 1 to 9.")
        continue
      if board[choice] != " ":
        print("That box is already taken. Choose another one.")
        continue
      break  # input is valid
    except ValueError:
      print("Invalid input. Please enter a number from 1 to 9.")
  board[choice] = current_player
  available.remove(choice)

# game loop
def play_game(board, mode):
  current_player = "x"
  value = random.randint(0, 1)
  if value == 0:
    player = mode
  else:
    player = 1
  for _ in range(9):  # max moves
    player = 1 if player == mode else mode
    current_player = play_turn(board, current_player, player)
    print_board(board)
    if check_winner(board):
      print_victory(player)
      return
  print_tie()

