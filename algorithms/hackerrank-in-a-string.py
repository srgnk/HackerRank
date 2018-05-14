#!/bin/python3

import sys

def hackerrankInString(s):
    hckr = list('hackerrank')
    index = 0
    res = ''
    
    for let in s:
        if index == len(hckr):
            break
        if let == hckr[index]:
            index += 1
    
    if index == len(hckr):
        res = 'YES'
    else:
        res = 'NO'
    return res

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
