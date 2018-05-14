#!/bin/python3

import sys

def powerSum(X, N, num):
    value = X - num**N
    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return powerSum(value, N, num+1) + powerSum(X, N, num+1)

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N, 1)
    print(result)
