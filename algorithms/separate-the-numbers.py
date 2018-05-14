#!/bin/python3

import sys

def validate(s, first):
    while s:
        if s.startswith(first):
            s = s[len(first):]
            first = str(int(first) + 1)
        else:
            return False
    return True

def separateNumbers(s):
    if s[0] == '0' and len(s) > 1:
        return "NO"
    else:
        for ind in range(1, len(s)//2 + 1):
            first = s[:ind]
            if validate(str(s), first):
                return "YES " + first
    return "NO"
            

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        print(separateNumbers(s))
