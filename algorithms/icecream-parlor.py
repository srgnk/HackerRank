#!/bin/python3

import sys

def solve(arr, money):
    # find matched number
    cost_map = {}
    for i, cost in enumerate(arr):
        johnny = money - cost
        #print("cost = {} johny = {}".format(cost, johnny))
        #print(cost_map.keys())
        #print(cost_map)
        if johnny in cost_map.keys():
            print("{} {}".format(cost_map[johnny]+1, i+1))
        else:
            cost_map[cost] = i
            
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)