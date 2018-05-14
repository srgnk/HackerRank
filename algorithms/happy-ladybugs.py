#!/bin/python3

import os
import sys
from collections import Counter

#
# Complete the happyLadybugs function below.
#

def is_happy(b):
    if b[0] != b[1] or b[-1] != b[-2]:
        return False
    for ind in range(1, len(b)-1):
        if b[ind] != b[ind-1] and b[ind] != b[ind+1]:
            return False
        
    return True

def happyLadybugs(b):
    cnt = Counter(b)
    print("cnt = {}".format(cnt))
    
    singles = list(filter(lambda x: x[0] != '_' and x[1] == 1, cnt.items()))
    empty = b.count('_')
    
    print("singles = {}".format(singles))
    print("empty = {}".format(empty))
    
    if len(singles) == 0 and empty > 0:
        return 'YES'
    elif len(b) > 2 and is_happy(b):
        return 'YES'
    else:
        return 'NO'
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
