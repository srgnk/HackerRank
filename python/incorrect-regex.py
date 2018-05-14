#!/usr/bin/env python3

import re

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        try:
            re.compile(input().strip())
            res = True
        except BaseException:
            res = False
        print(res)