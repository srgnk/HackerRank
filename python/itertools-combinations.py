#!/usr/bin/env python3

from itertools import combinations

if __name__ == "__main__":
    in_data = list(input().strip().split(' '))
    
    for lng in range(1, int(in_data[1])+1):
        for el in combinations(sorted(in_data[0]), lng):
            print("".join(el))