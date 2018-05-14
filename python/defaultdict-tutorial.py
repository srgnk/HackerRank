#!/usr/bin/env python3

from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    library = defaultdict(list)
    
    for ind in range(1, n + 1):
        word = input().strip()
        library[word].append(ind)
    
    for ind in range(m):
        word = input().strip()
        if len(library[word]) > 0:
            print(" ".join(map(str, library[word])))
        else:
            print("-1")
    