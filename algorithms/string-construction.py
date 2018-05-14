#!/bin/python3

import sys

def stringConstruction(s):
    return len(set(s))
        

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
