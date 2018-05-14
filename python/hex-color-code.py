import re

n = int(input().strip())
inside = False
for _ in range(n):
    line = input()
    
    for el in line.split(' '):
        if el == "{":
            inside = True
            continue
        elif el == "}":
            inside = False
            continue
        elif inside:
            found = re.search(r'\#[0-9a-fA-F]{3,6}', el)
            if found:
                print(found.group(0))