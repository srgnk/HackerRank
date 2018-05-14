#!/usr/bin/env python3

from itertools import product

if __name__ == "__main__":
    arr1 = list(map(int, input().strip().split(' ')))
    arr2 = list(map(int, input().strip().split(' ')))
    
    for el in product(arr1, arr2):
        print("{} ".format(el), end='')
    