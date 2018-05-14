#!/bin/python3

import sys

def countingSort(arr):
    output = [0] * (max(arr) + 1)
    
    for el in arr:
        output[el] += 1
        
    return output

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))


