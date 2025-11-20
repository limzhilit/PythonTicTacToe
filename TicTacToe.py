board = [[0 for _ in range(3)] for _ in range(3)]


for i, row in enumerate(board):
    print(" | ".join(map(str, row)))
    if i < len(board) - 1:  # print horizontal line between rows
        print("---+---+---")