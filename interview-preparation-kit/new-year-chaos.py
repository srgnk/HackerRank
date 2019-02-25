#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    res = 0
    
    for ind in range(len(q)):
        if q[ind] - (1+ind) > 2:
            return "Too chaotic"
        
    for ind in range(len(q)):
        for jnd in range(max(0, q[ind]-2), ind):
            if (q[jnd] > q[ind]):
                res += 1
                
    return res


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
