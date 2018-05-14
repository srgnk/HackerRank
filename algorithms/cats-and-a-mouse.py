#!/bin/python3

import sys

def catAndMouse(x, y, z):
    cat_a = abs(x - z)
    cat_b = abs(y - z)
    
    if cat_a < cat_b:
        return "Cat A"
    elif cat_a > cat_b:
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print ("".join(map(str, result)))


