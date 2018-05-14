cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    prev = 0
    cur = 1
    out = [prev, cur]
    
    for _ in range(n-2):
        prev, cur = cur, prev + cur
        out.append(cur)
        
    return out
        