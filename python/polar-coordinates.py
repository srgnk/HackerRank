#!/usr/bin/env python3

import cmath

if __name__ == "__main__":
    cnum = complex(input().strip())
    
    print(abs(cnum))
    print(cmath.phase(cnum))