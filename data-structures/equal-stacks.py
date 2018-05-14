#!/bin/python3

import sys

if __name__ == "__main__":
    n1,n2,n3 = input().strip().split(' ')
    n1,n2,n3 = [int(n1),int(n2),int(n3)]
    h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
    h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
    h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
    stacks = [h1[::-1], h2[::-1], h3[::-1]]
    stack_sums = [sum(stacks[i]) for i in range(3)]
    
    while len({stack_sums[i] for i in range(3)}) > 1:
        tallest_stack = max(stack_sums)
        index = stack_sums.index(tallest_stack)
        removed = stacks[index].pop()
        stack_sums[index] -= removed
        
    print(min([sum(stacks[i]) for i in range(3)]))
    
