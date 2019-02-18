#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

def nimGame(pile):
    res = reduce((lambda x, y: x ^ y), pile)

    if res == 0:
        return 'Second'
    else:
        return 'First'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
