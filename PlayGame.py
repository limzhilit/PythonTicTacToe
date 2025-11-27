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

  #push
