import re

num = input()
print(bool(re.match(r'^[1-9][\d]{5}$', num) and len(re.findall(r'(\d)(?=\d\1)', num))<2 ))