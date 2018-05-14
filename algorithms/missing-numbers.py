#!/bin/python3

import sys
from collections import Counter

def missingNumbers(arr, brr):
    acnt = Counter(arr)
    bcnt = Counter(brr)
    
    for el in acnt.items():
        #print("checking {}".format(el))
        get = bcnt.get(el[0])
        if get:
            bcnt[el[0]] -= el[1]
    
    bcnt = list(map(lambda x: x[0], (filter(lambda x: x[1] > 0, bcnt.items()))))
    bcnt = sorted(bcnt)
    
    return bcnt
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))


