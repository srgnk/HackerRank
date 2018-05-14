#!/bin/python3

import sys

def stones(n, a, b):
    return sorted(set([(n-1)*min(a, b) + x*abs(a-b) for x in range(n)]))


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print (" ".join(map(str, result)))
