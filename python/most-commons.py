#!/bin/python3

import sys
from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    best = Counter(s)
    sortit = sorted(best.items(), key = lambda x: (-x[1], x[0]))[:3]
        
    print("\n".join(x[0]+" "+str(x[1]) for x in sortit))
