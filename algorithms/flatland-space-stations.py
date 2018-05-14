#!/bin/python3

import sys

def flatlandSpaceStations(n, stations):
    stations = sorted(stations)
    res = stations[0]
    
    for ind in range(1, len(stations)):
        res = max(res, (stations[ind] - stations[ind-1])//2)
        
    res = max(res, n-1 - stations[-1])
        
    return res
        
    

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)
