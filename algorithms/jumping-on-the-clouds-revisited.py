#!/bin/python3

import sys

def jumpingOnClouds(c, k):
    cur = k % n
    energy = 100 - 1 - c[cur]*2
    
    while cur != 0:
        cur = (cur + k) % n
        energy -= 1 + c[cur]*2
        
    return energy

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
