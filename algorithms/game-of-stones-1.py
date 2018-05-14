#!/bin/python3

import sys

def gameOfStones(n):
    if n%7 == 1 or n%7 == 0:
        return 'Second'
    else:
        return 'First'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        print(result)
