#!/bin/python3

import math
import os
import random
import re
import sys

def how_many_games(p, d, m, s):
    res = 0

    while s > 0:
        res += 1
        s -= p
        p = max(p - d, m)

    if s != 0:
        res -= 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p, d, m, s = [int(n) for n in input().split(" ")]

    answer = how_many_games(p, d, m, s)

    fptr.write(str(answer) + '\n')
    fptr.close()
