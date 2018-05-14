#!/bin/python3

import sys

def hurdleRace(k, height):
    return max(0, max(height) - k)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
