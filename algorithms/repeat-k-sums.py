#!/usr/bin/env python3

from itertools import combinations_with_replacement

arr = []

def generate(arr, k):
    for el in combinations_with_replacement(arr, k):
        print(el, end=' ')
        
    print()
    
    for el in combinations_with_replacement(arr, k):
        print(sum(el), end=' ')
        
def delete_red(deep, output, ind, cur):
    global arr
    #print("go deep = {} ind = {} cur = {}".format(deep, ind, cur))
    if ind == 0:
        #print("arr is: {}".format(arr))
        #print("removing {}".format(cur))
        arr.remove(cur)
    else:
        while deep >= 0:
            #print("going deeper with: output = {} el = {}".format(output, output[deep]))
            delete_red(deep, output, ind-1, cur+output[deep])
            deep -= 1
    

def solution(n, k):
    global arr
    output = [arr[0]//k]
    del arr[0]
    
    for ind in range(1, n):
        #print("arr is now: {}".format(arr))
        el = arr[0] - (k-1)*output[0]
        #print("a[{}] = {} = {} - {}".format(ind, el, arr[ind], (k-1)*output[0]))
        #print("output is: {}".format(output))
        output.append(el)
        
        if ind < n-1:
            delete_red(ind, output, k-1, output[-1])
    
    return output

if __name__ == "__main__":
    #generate([1, 2, 10], k = 2)
    #print()
    #generate([1, 2, 10], k = 4)
    t = int(input().strip())
    
    for _ in range(t):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        arr = sorted(arr)
        print(" ".join(map(str, solution(n, k))))