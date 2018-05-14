#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _ in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
    
    print(sum(s))

