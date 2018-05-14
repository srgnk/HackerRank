import re

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        uid = "".join(sorted(input()))
        if (len(uid) == 10 and
            re.match(r'', uid) and 
            re.search(r'[A-Z]{2}', uid) and
            re.search(r'\d\d\d', uid) and
            not re.search(r'[^a-zA-Z0-9]', uid) and
            not re.search(r'(.)\1', uid)):
            print("Valid")
        else:
            print("Invalid")
                