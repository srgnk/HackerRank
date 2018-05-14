#!/bin/python3

import sys
from collections import Counter
from collections import defaultdict
from itertools import permutations
import math

def binomial(x, y):
    if y == x:
        return 1
    elif y == 1:         # see georg's comment
        return x
    elif y > x:          # will be executed only if y != 1 and y != x
        return 0
    else:                # will be executed only if y != 1 and y != x and x <= y
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x-y)  # that appears to be useful to get the correct result
        div = a // (b * c)
        return div

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

def sherlockAndAnagrams(s):
    res = 0
    handict = defaultdict(int)
    for sub in get_all_substrings(s):
        handict[str(sorted(sub))] += 1
        
    #print(list(filter(lambda x: x[1] != 1, handict.items())))
    for el in list(filter(lambda x: x[1] != 1, handict.items())):
        res += binomial(el[1], 2)
    
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
