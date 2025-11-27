from PlayGame import *

while True:
# representing board
  print("Welcome to TicTacToe)
  play = input("New Game? (y/n)")
  if play == 'n':
    break
  board = [" " for _ in range(9)]

  play_game(board)
