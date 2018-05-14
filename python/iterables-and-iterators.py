#!/usr/bin/env python3

import string
symbols = string.ascii_lowercase

from itertools import combinations

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(str, input().strip().split(' ')))
    times = int(input().strip())
    cmbts = list(combinations(sorted(arr), times))
    
    print("{:.4f}".format(len(list(filter(lambda a: a[0] == 'a', cmbts)))/(len(cmbts))))
    
    