#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

def misereNim(pile):
    if set(pile) == {1}:
        if len(pile)%2 == 0:
            return 'First'
        else:
            return 'Second'

    res = reduce((lambda x, y: x ^ y), pile)
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

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
