#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the nimbleGame function below.
def nimbleGame(s):
    if len(s) > 1:
        res = 0
        for ind, el in enumerate(s):
            if el%2 == 1:
                res ^= ind
    else:
        return 'Second'

    if res == 0:
        return 'Second'
    else:
        return 'First'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
