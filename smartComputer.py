from checkWin import check_winner
from PlayGame import *

winning_probability = [4,0,2,6,8,1,2,5,7]

def smart_move(board, current_player):
  copy = board.copy()
  other_player =  "o" if current_player == "x" else "x"

  # win in 1 move
  for i in range(9):
    if board[i] != " ":
      continue
    copy[i] = current_player
    if check_winner(copy) == 1:
      board[i] = current_player
      print(f"Computer chose {i}")
      return
    copy[i] = " "

  # lose in 1 move
  for i in range(9):
    if board[i] != " ":
      continue
    copy[i] = other_player
    if check_winner(copy) == 1:
      board[i] = current_player
      print(f"Computer chose {i+1}")
      return
    copy[i] = " "

  # possible win in 2 move
  empty_count = board.count(" ")
  if empty_count <= 4:
    for i in range(9):
      if copy[i] != " ":
        continue
      copy[i] = current_player
      if check_winner(copy) == 1:
        board[i] = current_player
        print(f"Computer chose {i+1}")
        return

  # best move otherwise
  for i in winning_probability:
    if board[i] != " ":
      continue
    board[i] = current_player
    print(f"Computer chose {i+1}")
    return
  return
