#!/bin/python3
# this should work

import sys
from math import factorial

def extraLongFactorials(n):
    return factorial(n)
    

if __name__ == "__main__":
    n = int(input().strip())
    print(extraLongFactorials(n))
