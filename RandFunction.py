

import random


def get_pc_pick():
    return random.choice(['X', 'O'])

pc_pick = get_pc_pick()
print("Computer Picked", pc_pick)