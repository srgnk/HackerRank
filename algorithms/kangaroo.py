#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if x1 >= x2 and v1 > v2:
        return 'NO'
    elif x2 >= x1 and v2 > v1:
        return 'NO'
    elif (x1 > x2 or x2 > x1) and v1 == v2:
        return 'NO'
    else:
        pos1, pos2 = x1, x2
        dif_prev = dif = abs(pos1 - pos2)
        while dif_prev >= dif:
            if pos1 == pos2:
                return 'YES'
            pos1 += v1
            pos2 += v2
            dif_prev, dif = dif, abs(pos1 - pos2)
    return 'NO'
            
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
