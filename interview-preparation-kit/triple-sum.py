#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    res = 0

    for el in b:
        left = bisect_right(a, el)
        right = bisect_right(c, el)

        print("left = {} el = {} right = {}".format(left, el, right))

        res += left * right

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
