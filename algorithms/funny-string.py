#!/bin/python3

import sys
import string

alpha = string.ascii_lowercase

def funnyString(s):
    res = 'Funny'
    r = s[::-1]
    
    for ind in range(1, len(s)):
        #print("{} - {} ?= {} - {}".format(alpha.index(s[ind]), alpha.index(s[ind-1]), alpha.index(r[ind]), alpha.index(r[ind-1])))
        if abs(alpha.index(s[ind]) - alpha.index(s[ind-1])) != abs(alpha.index(r[ind]) - alpha.index(r[ind-1])):
            res = 'Not Funny'
            break
            
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
