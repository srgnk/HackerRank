#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0
    ind = 0
    
    while ind < len(arr)-1:
        #print("ind = {} arr: {}".format(ind, arr))
        if arr[ind] == ind + 1:
            ind += 1
            continue
        else:
            arr[arr[ind]-1], arr[ind] = arr[ind], arr[arr[ind]-1]
            res += 1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
