#!/bin/python3

import sys
from math import inf

def dec_to_bin(number):
    return bin(number)[2:]

def bin_to_dec(number):
    return int(number, 2)

def buildup_to_len(number, length):
    return '0' * (length - len(number)) + number

def get_max_len(arr):
    return len(dec_to_bin(max(arr)))
    
def get_min_len(arr):
    return len(dec_to_bin(min(arr)))

def anotherMinimaxProblem(a):
    res = inf
    arr_bin = []
    
    if max(a) == min(a) and max(a) == 0:
        return 0
    
    for el in a:
        arr_bin.append(dec_to_bin(el))
    
    # trim the elements
    while len(max(arr_bin, key=len)) == len(min(arr_bin, key=len)):
        arr_bin = [ el[:1].lstrip('1') + el[1:] for el in arr_bin ]
        arr_bin = [ el.lstrip('0') for el in arr_bin ]
        
    # build up the lesser elements
    max_len = len(max(arr_bin, key=len))
    #print("max len = {}".format(max_len))
    arr_bin = [ buildup_to_len(el, max_len) for el in arr_bin ]
    
    arr_zeros = []
    arr_ones = []
    
    for el in sorted(arr_bin):
        if el[0] == '0':
            arr_zeros.append(el)
        else:
            arr_ones.append(el)
    
    for el_z in arr_zeros:
        for el_o in arr_ones:
            res = min(res, bin_to_dec(el_z) ^ bin_to_dec(el_o))
    
    return res

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = anotherMinimaxProblem(a)
    print(result)
