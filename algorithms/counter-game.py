#!/bin/python3
# naive method

import sys
import math

def get_mask(n):
    return 1 << math.floor(math.log(n,2))

def counter_game(n):
    winner = 0
    while n != 1:
        mask = get_mask(n)
        if mask == n:
            n = n/2
        else:
            n -= mask
            
        winner ^= 1
    
    
    if winner == 1:
        return "Louise"
    elif winner == 0:
        return "Richard"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = counter_game(n)
        print(result)
