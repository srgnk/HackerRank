#!/bin/python3

import sys

def gridChallenge(grid):
    res = 'YES'
    newgrid = []
    
    for row in grid:
        newgrid.append(sorted(row))
        
    #for row in newgrid:
    #    print(row)
        
    for ind in range(len(grid)):
        for jnd in range(ind, len(grid[0])):
            newgrid[ind][jnd], newgrid[jnd][ind] = newgrid[jnd][ind], newgrid[ind][jnd]
            
    for row in newgrid:
        if row != sorted(row):
            res = 'NO'
            break
            
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        grid_i = 0
        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(grid_t)
        result = gridChallenge(grid)
        print(result)
