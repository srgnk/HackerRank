#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    pairs = defaultdict(int)
    triplets = defaultdict(int)

    for el in arr:
        res += triplets[el]

        triplets[r*el] += pairs[el]
        pairs[r*el] += 1
        #print("el = {} triplets = {} pairs = {}".format(el, dict(triplets), dict(pairs)))

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
