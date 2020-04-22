#!/bin/python3

import sys
from collections import Counter

def equalizeArray(arr):
    print(len(arr) - Counter(arr).most_common(1)[0][1])
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
