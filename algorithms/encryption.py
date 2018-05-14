#!/bin/python3

import sys
from math import sqrt
from math import ceil

def get_grid(number):
    root = sqrt(number)
    
    x = int(root//1)
    y = ceil(root)
    
    while x*y < number:
        if x <= y:
            x += 1
        else:
            y += 1
        
    return (x, y)

def encryption(string):
    string = string.strip().replace(' ', '')
    str_len = len(string)
    
    x, y = get_grid(str_len)
    #print("x = {} y = {}".format(x, y))
    grid = [ [ '' for i in range(x) ] for _j in range(y) ]
    
    count = 0
    x_ind = 0
    y_ind = 0
    for ind in range(str_len):
        if count / y == 1 and count % y == 0:
            count = 0
            y_ind += 1
            x_ind = 0
            
        grid[x_ind][y_ind] = string[ind]
        count += 1
        x_ind += 1
        
    #print(grid)
    out = ''
    for _i in range(y):
        for _j in range(x):
            out += grid[_i][_j]
        out += ' '
    #print(out)
        
    #out = ''
    #for _i in range(y):
    #    for _j in range(x):
    #        out += grid[_i][_j]
    #    out += ' '

    return out
        
if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
