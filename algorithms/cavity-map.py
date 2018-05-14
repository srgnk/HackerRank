#!/bin/python3

import sys

def cavityMap(grid):
    leng = len(grid)
    output = [[0]*leng for _ in range(leng)]
    
    for ind in range(leng):
        for jnd in range(leng):
            if (0 < ind < leng-1 and 0 < jnd < leng-1 and
               grid[ind][jnd] > grid[ind+1][jnd] and
               grid[ind][jnd] > grid[ind-1][jnd] and
               grid[ind][jnd] > grid[ind][jnd+1] and
               grid[ind][jnd] > grid[ind][jnd-1]):
                output[ind][jnd] = 'X'
            else:
                output[ind][jnd] = grid[ind][jnd]
    
    return output

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
        grid_t = list(map(int, input().strip()))
        grid.append(grid_t)
    result = cavityMap(grid)
    print("\n".join(["".join(map(str, x)) for x in result]))


