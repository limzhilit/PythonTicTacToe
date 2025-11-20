# play game feature to so user can choose boxes, mark boxes and
# alternate between player moves

# representing board
board = [" " for _ in range(9)]

# function to display board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# function to switch player
def switch_player(current):
    return "O" if current == "X" else "X"

# core method to play a turn
def play_turn(board, current_player):
    # ask the current player for a position 1–9
    choice = int(input(f"Player {current_player}, choose a box (1-9): ")) - 1

    # make sure it’s empty
    if board[choice] == " ":
        board[choice] = current_player
    else:
        print("That spot is taken! Try again.")
        return current_player  # same player tries again

    return switch_player(current_player)

# game loop
def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    for _ in range(9):  # max moves
        print_board(board)
        current_player = play_turn(board, current_player)

    print_board(board)
    print("Game over!")