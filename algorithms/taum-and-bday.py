#!/bin/python3

import os
import sys

#
# Complete the taumBday function below.
#
def taumBday(b, w, bc, wc, z):
    res = 0
    
    if bc <= wc:
        res += bc*b
        if bc + z <= wc:
            res += (bc + z)*w
        else:
            res += wc*w
    else:
        res += wc*w
        if wc + z <= bc:
            res += (wc + z)*b
        else:
            res += bc*b
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
