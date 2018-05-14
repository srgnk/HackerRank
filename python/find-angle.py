#!/usr/bin/env python3

from math import atan
from math import degrees

if __name__ == "__main__":
    ab = int(input().strip())
    bc = int(input().strip())
    
    print("{}°".format(int(round(degrees(atan(ab/bc))))))