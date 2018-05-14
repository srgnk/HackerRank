#!/usr/bin/env python3

import re

if __name__ == "__main__":
    string = input()
    
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    
    print(match.group(1) if match else -1)
    