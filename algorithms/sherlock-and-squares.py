#!/bin/python3

import sys
from math import ceil, floor

def squares(a, b):
    res = 0
    res = floor(b**0.5)+1 - ceil(a**0.5)
    return res

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
