#!/usr/bin/env python3

import re

if __name__ == "__main__":
    out = list(re.split('[.,]', input()))
    print("\n".join(filter(lambda x: re.match('[0-9]+',x), out)))