#!/bin/python3

import math
import os
import random
import re
import sys

def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n]

# Complete the commonChild function below.
def commonChild(s1, s2):
    common_letters = set(s1) & set(s2)

    print("intersect: {}".format(common_letters))

    if (not bool(common_letters)):
        return 0

    s1_filt = "".join([x for x in s1 if x in common_letters])
    s2_filt = "".join([x for x in s2 if x in common_letters])

    print("s1_filt: {}".format(s1_filt))
    print("s2_filt: {}".format(s2_filt))

    #return LCSubStr(s1_filt, s2_filt, len(s1_filt), len(s2_filt))
    return lcs(s1, s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

