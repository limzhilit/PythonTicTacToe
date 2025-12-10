import random
from turtledemo.sorting_animate import enable_keys

def pcMove(board, current_player, available):
    move = random.choice(available)  # always safe, always empty
    board[move] = current_player
    available.remove(move)
    print("PC picked:", move + 1)
