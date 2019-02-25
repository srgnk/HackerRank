def staircase(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return staircase(n-1) + staircase(n-2) + staircase(n-3)

def staircase_lin(n):
    st1, st2, st3 = 1, 2, 4
    
    for _ in range(n-1):
        st1, st2, st3 = st2, st3, st1 + st2 + st3

    return st1

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(staircase_lin(n))