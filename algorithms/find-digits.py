#!/bin/python3

import sys

def findDigits(n):
    res = 0
    for dig in n:
        if dig != '0' and int(n) % int(dig) == 0:
            res += 1
        
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = input().strip()
        result = findDigits(n)
        print(result)
