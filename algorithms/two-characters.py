#!/bin/python3

import sys
from itertools import combinations

def validate(string):
    for ind in range(len(string)-1):
        if string[ind] == string[ind + 1]:
            return False
    return True

def twoCharaters(string):
    str_set = set(list(string))
    variants = combinations(str_set, 2)
    max_res = 0
    
    for comb in variants:
        t = [c for c in string if c == comb[0] or c == comb[1]]
        #print("comb = {} t = {}".format(comb, t))
        if validate(t):
            max_res = max(max_res, len(t))
        
    return max_res
    

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
