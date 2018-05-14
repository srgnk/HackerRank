#!/bin/python3

import sys
from collections import defaultdict
from math import fabs

def check_diag(queen, obst):
    if queen[1] == obst[1]:
        return 0
    check = (queen[0] - obst[0])/(queen[1] - obst[1])
    if fabs(check) == 1.0:
        return int(check)
    else:
        return 0

def queensAttack(n, k, r_q, c_q, obstacles):
    queen = [r_q, c_q]
    res = 0
    obst_by_row = list(filter(lambda x: x[0] == r_q, obstacles))
    obst_by_col = list(filter(lambda x: x[1] == c_q, obstacles))
    obst_by_plus_diag = list(filter(lambda x: check_diag(queen, x) == 1, obstacles))
    obst_by_neg_diag = list(filter(lambda x: check_diag(queen, x) == -1, obstacles))
    
    if not obst_by_col:
        res += n-1
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_col)) 
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[0]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_col)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[0]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2
            
    if not obst_by_row:
        res += n-1
    else:
        obst_higher = list(filter(lambda x: x[1] > c_q, obst_by_row)) 
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[1])[1]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[1] < c_q, obst_by_row)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[1])[1]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2
        
    # diagonals
    if not obst_by_plus_diag:
        res += n-1 - abs(r_q - c_q)
        #res += min(n - c_q, n - r_q) + min(c_q - 1, r_q - 1) # = n-1 + min(-c_q, -r_q) + min(c_q, r_q)
        #print("res = {}".format(res))
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_plus_diag))
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[0]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_plus_diag)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[0]
        else:
            max_lower = 0
            
        #print("high = {} low = {}".format(min_higher, max_lower))
        res += min_higher - max_lower - 2 - abs(r_q - c_q)
    
    if not obst_by_neg_diag:
        #print("n - c_q + r_q = {} - {} + {}".format(n, c_q, r_q))
        #res += n-1 - abs(n - c_q + r_q)
        #print("res = {}".format(res))
        #res += min(n - c_q, r_q - 1) + min(c_q - 1, n - r_q)
        # 2 variants:
        # res += n - c_q + n - r_q = 2n - c_q - r_q
        # res += r_q - 1 + c_q - 1 = r_q + c_q - 2
        res += min(n - c_q, r_q - 1)
        res += min(c_q - 1, n - r_q)
    else:
        obst_higher = list(filter(lambda x: x[0] > r_q, obst_by_neg_diag))
        if obst_higher:
            min_higher = min(obst_higher, key = lambda x: x[0])[1]
        else:
            min_higher = n+1
            
        obst_lower = list(filter(lambda x: x[0] < r_q, obst_by_neg_diag)) 
        if obst_lower:
            max_lower = max(obst_lower, key = lambda x: x[0])[1]
        else:
            max_lower = 0
            
        print("high = {} low = {}".format(min_higher, max_lower))
        print("r_q = {} c_q = {}".format(r_q, c_q))
        #res += min_higher - max_lower - 2 - abs(n - c_q + r_q)
        if max_lower != 0:
            res += max_lower - c_q - 1
        if min_higher != n+1:
            res += c_q - min_higher - 1
 
    return res
        
    
# naive        
def queensAttack_naive(n, k, r_q, c_q, obstacles):
    obst_by_row = list(filter(lambda x: x[0] == r_q, obstacles))
    obst_by_col = list(filter(lambda x: x[1] == c_q, obstacles))
    obs_dict = gen_obs_dict(obstacles)
    
    res = 0
    
    if not obst_by_col:
        res += n-1
    else:
        for row_ind in range(r_q+1, n+1):
            #if not [row_ind, c_q] in obstacles:
            key = str(row_ind) + "-" + str(c_q)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
        for row_ind in range(r_q-1, 0, -1):
            #if not [row_ind, c_q] in obstacles:
            key = str(row_ind) + "-" + str(c_q)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
            
    if not obst_by_row:
        res += n-1
    else:
        for col_ind in range(c_q+1, n+1):
            #if not [r_q, col_ind] in obstacles:
            key = str(r_q) + "-" + str(col_ind)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
        for col_ind in range(c_q-1, 0, -1):
            #if not [r_q, col_ind] in obstacles:
            key = str(r_q) + "-" + str(col_ind)
            if obs_dict[key] != -1:
                res += 1
            else:
                break
    
    row_ind, col_ind = r_q+1, c_q+1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind += 1
            col_ind += 1
        else:
            break
            
    row_ind, col_ind = r_q-1, c_q+1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind -= 1
            col_ind += 1
        else:
            break
            
    row_ind, col_ind = r_q+1, c_q-1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind += 1
            col_ind -= 1
        else:
            break        
            
    row_ind, col_ind = r_q-1, c_q-1
    while col_ind != 0 and row_ind != 0 and col_ind != n+1 and row_ind != n+1:
        #if not [row_ind, col_ind] in obstacles:
        key = str(row_ind) + "-" + str(col_ind)
        if obs_dict[key] != -1:
            res += 1
            row_ind -= 1
            col_ind -= 1
        else:
            break        
 
    return res
            
def gen_obs_dict(obstacles):
    dict_out = defaultdict(int)    
    for obs in obstacles:
        row, col = obs[0], obs[1]
        key = str(row) + "-" + str(col)
        dict_out[key] = -1
        
    return dict_out

if __name__ == "__main__":
    n, k = [int(x) for x in input().strip().split(' ')]
    r_q, c_q = [int(x) for x in input().strip().split(' ')]
    obstacles = []
    for obstacles_i in range(k):
        obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
        obstacles.append(obstacles_t)
    result = queensAttack_naive(n, k, r_q, c_q, obstacles)
    print(result)
