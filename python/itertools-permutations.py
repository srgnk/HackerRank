#!/usr/bin/env python3

from itertools import permutations

if __name__ == "__main__":
    in_data = list(input().strip().split(' '))
    
    for el in permutations(sorted(in_data[0]), int(in_data[1])):
        print("".join(el))