#!/bin/python3

import sys
import copy

def find_plus(grid, x, y, mx):
    n = len(grid)
    m = len(grid[0])
    deep = 0
    no_more = 0
    i = 1
    if grid[x][y] != 1:
        return 0, no_more
    
    while (x+i < n and x-i >= 0 and y+i < m and y-i >= 0 and
          grid[x+i][y] == 1 and grid[x-i][y] == 1 and
          grid[x][y+i] == 1 and grid[x][y-i] == 1 and
          deep < mx):
        grid[x+i][y] = 2
        grid[x-i][y] = 2
        grid[x][y+i] = 2
        grid[x][y-i] = 2
        i += 1
        deep += 1
        
    if i > 1:
        grid[x][y] = 2
        
    if mx >= i:
        no_more = 1
        
    return 1 + 4*(i-1), no_more

def find_pair(grid, x, y):
    res = 1
    best_x = 0
    best_y = 0
    for ind in range(x, n):
        for jnd in range(m):
            if ind == x and jnd <= y:
                continue
            matrix = copy.deepcopy(grid)
            temp_res, ign = find_plus(matrix, ind, jnd, max(n, m)+1)
            if temp_res > res:
                res = max(res, temp_res)
                best_x = ind
                best_y = jnd
                #print("FIRST: x = {} y = {}".format(x, y))
                #print("SECON: x = {} y = {} found best!".format(ind, jnd))
            
    #print("Secon: x = {} y = {} square = {}".format(best_x, best_y, res))
            
    return res, best_x, best_y

def twoPluses(grid):
    res = 0
    n = len(grid)
    m = len(grid[0])
    b_x_1 = 0
    b_y_1 = 0
    b_x_2 = 0
    b_y_2 = 0
    b_1 = 0
    b_2 = 0
    
    for row in grid:
        for el in row:
            if el == 1:
                res = 1
                break
    
    for ind in range(n):
        for jnd in range(m):
            for mx in range(max(n, m)+1):
                matrix = copy.deepcopy(grid)
                first, skip = find_plus(matrix, ind, jnd, mx)
                if first == 0 or skip == 1:
                    continue
                #print("First: x = {} y = {} deep = {} skip = {} square = {}".format(ind, jnd, mx, skip, first))
                second, t_x, t_y = find_pair(matrix, ind, jnd)
                if first * second > res:
                    res = max(res, first*second)
                    b_x_1 = ind
                    b_y_1 = jnd
                    b_1 = first
                    b_x_2 = t_x
                    b_y_2 = t_y
                    b_2 = second
                #print("Result: {}".format(res))
                #print_grid(matrix)
    
    #print("BEST First: x = {} y = {} square = {}".format(b_x_1, b_y_1, b_1))
    #print("BEST Secon: x = {} y = {} square = {}".format(b_x_2, b_y_2, b_2))
    return res

def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end='')
        print()

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    grid = []
    grid_i = 0
    for grid_i in range(n):
        grid_t = str(input().strip())
        grid.append(grid_t)
        
    grid_norm = [[0]*m for _ in range(n)]
        
    for ind in range(n):
        for jnd in range(m):
            if grid[ind][jnd] == 'G':
                grid_norm[ind][jnd] = 1
    
    result = twoPluses(grid_norm)
    print(result)
