#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    output = []
    uniq = list(sorted(list(set(scores)), reverse=True))
    last = len(uniq)
    
    for cur in alice:
        #print("cur = {} last = {}".format(cur, last))
        while last > 0 and cur > uniq[last-1]:
            #print("DOWN {} -> {}".format(last, last-1))
            last -= 1
        if cur == uniq[last-1]:
            output.append(last)
        else:
            output.append(last+1)
        
    return output

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))


