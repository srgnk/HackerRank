#!/bin/python3

import sys

def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        return 1 if n%2 == 1 else 2
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        result = towerBreakers(n, m)
        print(result)
