#!/bin/python3

import sys

answers = [1]

def gen_answers():
    newlen = 1
    for i in range(61):
        if i % 2 == 1:
            newlen += 1
        else:
            newlen *= 2
        answers.append(newlen)
        

def utopianTree(n):
    return answers[n]

if __name__ == "__main__":
    t = int(input().strip())
    gen_answers()
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
