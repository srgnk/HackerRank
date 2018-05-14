#!/usr/bin/env python3

from collections import OrderedDict

if __name__ == "__main__":
    num = int(input().strip())
    history = OrderedDict()
    
    for _ in range(num):
        word = str(input().strip().split())
        if word not in history.keys():
            history[word] = 1
        else:
            history[word] += 1
            
    print(len(history.keys()))
    print(" ".join(map(str, history.values())))
