#!/bin/python3

import sys

def plusMinus(arr):
    arrlen = len(arr)
    positive = negative = zeros = 0
    
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
        else:
            zeros += 1
            
    print("{:.6f}\n{:.6f}\n{:.6f}".format(positive/arrlen, negative/arrlen, zeros/arrlen))
            

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
