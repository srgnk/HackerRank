#!/bin/python3

import sys

def marcsCakewalk(arr):
    arr = sorted(arr, key = lambda x: -x)
    
    return sum([el * (2**mult) for mult, el in enumerate(arr)])

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)
