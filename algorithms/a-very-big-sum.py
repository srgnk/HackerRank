#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    sum = 0
    for elem in ar:
        sum += elem
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
