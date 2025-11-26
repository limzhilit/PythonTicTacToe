from FunctionToDisplayBoard import print_board
from checkWin import *
# play game feature to so user can choose boxes, mark boxes and
# alternate between player moves

# function to switch player
def switch_player(current):
  return "o" if current == "x" else "x"

# core method to play a turn
def play_turn(board, current_player):
  while True:
  # ask the current player for a position 1–9
    choice = int(input(f"Player {current_player}, choose a box (1-9): ")) - 1
  # make sure it’s empty
    if board[choice] == " ":
      board[choice] = current_player
      break
    else:
      print("That spot is taken! Try again.")
  return switch_player(current_player)


# game loop
def play_game(board):
  current_player = "x"
  for _ in range(9):  # max moves
    current_player = play_turn(board, current_player)
    print_board(board)
    if check_winner(board):
      print_victory()
      return
  print_tie()
