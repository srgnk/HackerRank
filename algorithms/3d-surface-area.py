#!/bin/python3

import sys

def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2*H*W
    #print("H = {} W = {} area = {}".format(len(A), len(A[0]), area))
    
    for ind in range(H):
        for jnd in range(W):
            #print("i = {} j = {} A = {}".format(ind, jnd, A[ind][jnd]))
            # ind-1, jnd
            if ind-1 >= 0:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind-1][jnd])))
                area += max(0, A[ind][jnd] - A[ind-1][jnd])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind, jnd-1
            if jnd-1 >= 0:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind][jnd-1])))
                area += max(0, A[ind][jnd] - A[ind][jnd-1])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind+1, jnd
            if ind+1 < H:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind+1][jnd])))
                area += max(0, A[ind][jnd] - A[ind+1][jnd])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
            # ind, jnd+1
            if jnd+1 < W:
                #print("adding part {}".format(max(0, A[ind][jnd] - A[ind][jnd+1])))
                area += max(0, A[ind][jnd] - A[ind][jnd+1])
            else:
                #print("adding full {}".format(A[ind][jnd]))
                area += A[ind][jnd]
    return area

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result)
