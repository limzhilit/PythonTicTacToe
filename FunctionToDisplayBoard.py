
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def print_board(board):
    display = []
    for i in range(9):
        if board[i] == " ":
            display.append(f"{CYAN}{i+1}{RESET}")
        else:
            display.append(f"{WHITE}{board[i]}{RESET}")

    print(display[0] + "|" + display[1] + "|" + display[2])
    print("-+-+-")
    print(display[3] + "|" + display[4] + "|" + display[5])
    print("-+-+-")
    print(display[6] + "|" + display[7] + "|" + display[8])
