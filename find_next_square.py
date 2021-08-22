import math

def find_next_square(sq):
    if sq == 0:
        return 0
    if sq % math.sqrt(sq) != 0:
        return -1
    else:
        return (math.sqrt(sq) + 1) * (math.sqrt(sq) + 1)