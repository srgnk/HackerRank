#!/bin/python3

import sys
from collections import Counter

def gameOfThrones(s):
    cnt = Counter(s)
    if len(s)%2 == 0:
        ret = all([x%2 == 0 for x in cnt.values()])
    else:
        if len(list(filter(lambda x: x%2 == 1, cnt.values()))) == 1:
            ret = True
        else:
            ret = False
            
    return 'YES' if ret else 'NO'

s = input().strip()
result = gameOfThrones(s)
print(result)
