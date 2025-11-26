board = [" " for _ in range(9)]  #sets range from 1-9 to enter 'X' or '0'

def print_board(board):
    """ Displays the current state of the board. """
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-+-+-")
