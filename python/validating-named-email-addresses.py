import re

t = int(input().strip())
for _ in range(t):
    name, email = input().strip().split()
    
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print("{} {}".format(name, email))