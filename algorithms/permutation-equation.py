#!/usr/bin/env python3

import sys

def permutationEquation(p):
    output = []
    
    for num in range(1, max(p)+1):
        output.append(p.index(p.index(num)+1)+1)
        
    return output
    

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))


