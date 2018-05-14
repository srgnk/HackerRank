import re

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        num = "".join(input())
        if (re.match(r'^[456]', num) and
            (re.match(r'([\d]{4}-){3}[\d]{4}$', num) or
             re.match(r'[\d]{16}', num)) and
            not re.search(r'(\d)\1{3,}', num.replace("-", ""))):
            print("Valid")
        else:
            print("Invalid")
