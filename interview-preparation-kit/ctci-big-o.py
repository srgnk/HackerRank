def is_prime(num):
    if num < 2:
        return False
    else:
        sqrt = int(num**(1/2))
        for i in range(2,sqrt+1):
            if n % i == 0:
                return False
    return True
        
        

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
