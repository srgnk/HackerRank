#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _i in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'intersection_update':
            get_set = set(map(int, input().split(' ')))
            s &= get_set
        elif cmd[0] == 'update':
            get_set = set(map(int, input().split(' ')))
            s |= get_set
        elif cmd[0] == 'difference_update':
            get_set = set(map(int, input().split(' ')))
            s -= get_set
        elif cmd[0] == 'symmetric_difference_update':
            get_set = set(map(int, input().split(' ')))
            s ^= get_set
    
    print(sum(s))
