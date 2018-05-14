#!/usr/bin/env python3

if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    
    for _ in range(q):
        d = int(input().strip())
        maxes = []
        was_first = False
        
        for i in range(n - d + 1):
            if i == 0 or was_first == True:
                #print(arr[i:i+d])
                maxes.append(max(arr[i:i+d]))
            else:
                #print("max({}, {})".format(maxes[-1], arr[i+d-1]))
                maxes.append(max(maxes[-1], arr[i+d-1]))
                
            if maxes[-1] == arr[i]:
                was_first = True
            else:
                was_first = False
            
        print(min(maxes))
            