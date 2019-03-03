#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    squashed = []
    cur = s[0]
    cnt = 0
    res = 0

    for el in s:
        if el != cur:
            squashed.append((cur, cnt))
            cur = el
            cnt = 1
        else:
            cnt += 1
    squashed.append((cur, cnt))

    print(squashed)

    for el in squashed:
        res += (el[1]*(1 + el[1]))//2

    for ind in range(len(squashed)-2):
        if squashed[ind][0] == squashed[ind+2][0] and squashed[ind+1][1] == 1:
            res += min(squashed[ind][1], squashed[ind+2][1])

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
