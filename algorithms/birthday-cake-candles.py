#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
