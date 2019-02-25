#!/bin/python3

import sys

def twoStrings(s1, s2):
    if len(set(s1) & set(s2)) > 0:
        return 'YES'
    else:
        return 'NO'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
