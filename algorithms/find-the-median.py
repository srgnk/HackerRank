#!/bin/python3

import sys

def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr)//2]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)
