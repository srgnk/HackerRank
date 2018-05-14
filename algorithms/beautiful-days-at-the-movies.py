#!/bin/python

import sys

def is_beautiful(num, k):
    rev_num = int(str(num)[::-1])
    return abs(num - rev_num)%k == 0

def beautifulDays(i, j, k):
    res = 0
    for num in  range(i, j+1):
        if is_beautiful(num, k):
            res += 1
    return res

if __name__ == "__main__":
    i, j, k = raw_input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print result
