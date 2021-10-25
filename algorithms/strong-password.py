#!/bin/python3

import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    res = 0

    n_bool = 1
    l_bool = 1
    u_bool = 1
    s_bool = 1
    for c in password:
        if c in numbers: n_bool = 0
        elif c in lower_case: l_bool = 0
        elif c in upper_case: u_bool = 0
        elif c in special_characters: s_bool = 0
    return max(6-n, n_bool + l_bool + u_bool + s_bool)


if __name__ == '__main__':
    

    n = int(input().strip())
    password = input()

    answer = minimumNumber(n, password)
    print(answer)
