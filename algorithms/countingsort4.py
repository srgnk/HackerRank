#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    array = []
    print_dict = {}
    for a0 in range(n):
        x, s = input().strip().split(' ')
        x, s = [int(x), str(s)]
        
        if a0 < n//2:
            array.append((x, "-"))
        else:
            array.append((x, s))
            
    print(" ".join(map(lambda x: x[1], sorted(array, key = lambda x: x[0]))))
