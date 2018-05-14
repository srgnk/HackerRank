#!/bin/python3

import sys

def generate_seive():
    limit = pow(10, 6) + 1
    seive = [-1]* limit
    seive[0], seive[1], seive[2], seive[3] = 0, 1, 2, 3
    
    for iind in range(limit):
        if seive[iind] == -1 or seive[iind] > seive[iind-1] + 1:
            seive[iind] = seive[iind-1] + 1
            
        jind = 1
        while jind <= iind and jind * iind < limit:
            if seive[jind * iind] == -1 or seive[jind * iind] > seive[iind] + 1:
                seive[jind * iind] = seive[iind] + 1
            jind += 1
    
    return seive

if __name__ == "__main__":
    Q = int(input().strip())
    seive = generate_seive()
    for a0 in range(Q):
        N = int(input().strip())
        print(seive[N])
