#!/usr/bin/env python3

import sys

def gen_primes(n):
    nroot = int(n**(0.5))
    sieve = list(range(n+1))
    sieve[1] = 0
    
    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    
    return [x for x in sieve if x !=0]

if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    plates = list(map(int, input().strip().split(' ')))
    primes = gen_primes(10000)
    
    b_stacks = []
    plate_stacks = [plates, []]
    for ind in range(q):
        a_ind = int(ind % 2)
        b = []
        while len(plate_stacks[a_ind]) > 0:
            pl = plate_stacks[a_ind].pop()
            if pl % primes[ind] == 0:
                b.append(pl)
            else:
                plate_stacks[1 - a_ind].append(pl)
        b_stacks.append(b)
            
    for b in b_stacks:
        if len(b) > 0:
            print(*b[::-1], sep='\n')
    for pl in plate_stacks:
        if len(pl) > 0:
            print(*pl[::-1], sep='\n')
