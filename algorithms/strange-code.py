#!/bin/python3

import os
import sys
import math

#
# Complete the strangeCounter function below.
#
def strangeCounter(t):
    base = math.log2((t + 2)/3)
    val_top = 3*2**(math.floor(base))
    print("base = {} base_t = {}".format(base, val_top))
    
    return val_top - (t - (val_top-2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
