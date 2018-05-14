#!/usr/bin/env python3

import sys
sys.setrecursionlimit(20000)


def mature_check(passwords, attempt):
    allpass = "".join(passwords)
    res = True
    for letter in attempt:
        if letter not in allpass:
            res = False
            break
    return res

def password_cracker(passwords, attempt, solution, memo):
    #print("solution = {} attempt = {} memo = {}".format(solution, attempt, memo))
    if len(attempt) == 0:
        return True
    
    if attempt in memo:
        return False
    
    for psw in passwords:
        if attempt.startswith(psw):
            solution.append(psw)
            
            memo[attempt] = True
            
            if password_cracker(passwords, attempt[len(psw):], solution, memo) == True:
                return True
            
            solution.pop()
            
    return False
            

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passwords = input().strip().split(' ')
        attempt = input().strip()
        solution = []
        memo = {}
        if mature_check(passwords, attempt) and password_cracker(passwords, attempt, solution, memo):
            print(" ".join(solution))
        else:
            print("WRONG PASSWORD")