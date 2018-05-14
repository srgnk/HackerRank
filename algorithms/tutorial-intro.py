#!/bin/python3

import sys

def introTutorial(V, arr):
    return arr.index(V)

if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = introTutorial(V, arr)
    print(result)
