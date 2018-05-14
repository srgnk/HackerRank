#!/bin/python3

import sys

def cutTheSticks(arr):
    out = []
    while arr:
        out.append(len(arr))
        arr_min = min(arr)
        arr = list(map(lambda x: x - arr_min, arr))
        arr = list(filter(lambda x: x > 0, arr))
        
        
    return out
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr)
    print ("\n".join(map(str, result)))


