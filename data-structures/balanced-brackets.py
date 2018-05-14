#!/bin/python3

import sys

def isBalanced(s):
    stack = []
 
    for letter in s:
        if letter == '{':
            stack.append(1)
        elif letter == '[':
            stack.append(2)
        elif letter == '(':
            stack.append(3)
        elif letter == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
        elif letter == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != 2:
                return False
        elif letter == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != 3:
                return False
 
    return len(stack) == 0

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        if result is True:
            print('YES')
        else:
            print('NO')
