SIZE = 3

def print_victory(player):
  if player == 1:
    print("You won, game is over\n")
  else:
    print("You lost, game is over\n")

def print_defeat():
  print("You lost, game is over\n")

def print_tie():
  print("It's a tie, game is over\n")

def check_winner(board):
  # checking rows
  for row in range(SIZE):
    if (board[0 + 3 * row] == board[1 + 3 * row] == board[2 + 3 * row]) and (board[0 + 3 * row] in ['x', 'o']):
      return 1

  # checking columns
  for col in range(SIZE):
    if (board[0+col] == board[3+col] == board[6+col]) and (board[0+col] in ['x', 'o']):
      return 1

  # checking main diagonal
  if board[0] == board[4] == board[8] and (board[0] in ['x', 'o']):
    return 1

  # checking anti-diagonal
  if board[2] == board[4] == board[6] and (board[2] in ['x', 'o']):
    return 1

  return 0
