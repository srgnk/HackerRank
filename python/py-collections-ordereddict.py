#!/usr/bin/env python3

from collections import OrderedDict

if __name__ == "__main__":
    num = int(input().strip())
    history = OrderedDict()
    
    for _ in range(num):
        get_log = input().strip().split()
        good = " ".join(get_log[:-1])
        sold = int(get_log[-1])
        if good not in history.keys():
            history[good] = sold
        else:
            history[good] += sold
            
        
    for key in history.keys():
        print("{} {}".format(key, history[key]))
    