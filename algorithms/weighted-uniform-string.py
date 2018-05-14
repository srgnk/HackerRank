#!/usr/bin/env python3

import sys
import string

symbols = string.ascii_lowercase

def gen_uniforms(s):
    uniforms = {}
    
    mult = 1
    let_prev = ''
    for let in s:
        if let == let_prev:
            mult += 1
        else:
            mult = 1
        
        let_prev = let
        uniforms[((symbols.index(let) + 1)*mult)] = True
            
    return uniforms
    

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    uniforms = gen_uniforms(s)
    
    for a0 in range(n):
        x = int(input().strip())
        
        if x in uniforms:
            print("Yes")
        else:
            print("No")
