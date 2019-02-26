#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    cnt = Counter(s)
    res = 'NO'
    print("cnt = {} len = {}".format(cnt, len(set(cnt.values()))))

    if len(set(cnt.values())) == 1:
        res = 'YES'
    elif len(set(cnt.values())) == 2:
        bigger = max(cnt.values())
        lesser = min(cnt.values())
        bigger_let = [let for let, c in cnt.items() if c == bigger]
        lesser_let = [let for let, c in cnt.items() if c == lesser]

        if len(lesser_let) == 1 and lesser == 1:
            res = 'YES'
        elif len(bigger_let) == 1 or len(lesser_let) == 1:
            if abs(bigger-lesser) == 1:
                res = 'YES'
            else:
                res = 'NO'
        else:
            res = 'NO'
    else:
        res = 'NO'

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
