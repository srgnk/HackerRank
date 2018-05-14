import re

n = int(input().strip())

for _ in range(n):
    tel = input().strip()
    pattern = '^[789][0-9]{9}$'
    print("{}".format("YES" if bool(re.match(pattern, tel)) else "NO"))