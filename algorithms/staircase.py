#!/bin/python3

import sys

def staircase(n):
    for i in range(n):
        for j in range(1, n+1):
            if i + j >= n:
                print("#", end='')
            else:
                print(" ", end='')
        print()

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
