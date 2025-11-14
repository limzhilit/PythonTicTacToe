SIZE = 3

def print_victory():
    print("You won, game is over")

def print_defeat():
    print("You lost, game is over")

def check_winner(board, data):
    # checking rows
    for row in range(SIZE):
        if board[row][0] == board[row][1] == board[row][2]:
            if data % 2 == 0:
                print_victory()
            else:
                print_defeat()
            return 1

    # checking columns
    for col in range(SIZE):
        if board[0][col] == board[1][col] == board[2][col]:
            if data % 2 == 0:
                print_victory()
            else:
                print_defeat()
            return 1

    # checking main diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if data % 2 == 0:
            print_victory()
        else:
            print_defeat()
        return 1

    # checking anti-diagonal
    if board[2][0] == board[1][1] == board[0][2]:
        if data % 2 == 0:
            print_victory()
        else:
            print_defeat()
        return 1

    return 0
