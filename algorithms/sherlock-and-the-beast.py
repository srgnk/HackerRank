#!/bin/python3

import sys

def find_number(n):
    three = n//3
    
    while (n - 3*three)%5 != 0:
        #print("three = {} five = {}".format(three, (n - 3*three)//5))
        three -= 1
        
    if three > 0:
        res = [5] * 3 * three
        res += [3] * (n - 3*three)
    elif three == 0 and n%5 == 0:
        res = [3] * n
    else:
        res = [-1]
        
    return res


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print("".join(map(str, find_number(n))))
