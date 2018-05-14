#!/usr/bin/env python3

import string
alphabet = string.ascii_lowercase

def is_pangram(s):
    return set(alphabet) < set(s.lower())

if __name__ == "__main__":
    if is_pangram(input().strip()):
        print("pangram")
    else:
        print("not pangram")