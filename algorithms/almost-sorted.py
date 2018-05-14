#!/bin/python3

import sys

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def almostSorted(arr):
    swap_l = -1
    swap_r = -1
    for ind in range(1, len(arr)):
        if arr[ind - 1] > arr[ind]:
            swap_l = ind - 1
            break
            
    for ind in range(swap_l + 1, len(arr)):
        if ind == len(arr) - 1 or arr[ind + 1] > arr[swap_l]:
            swap_r = ind
            arr[swap_l], arr[swap_r] = arr[swap_r], arr[swap_l]
            break
            
    if is_sorted(arr):
        print("yes")
        print("swap {} {}".format(swap_l + 1, swap_r + 1))
        return True
    
    arr[swap_l], arr[swap_r] = arr[swap_r], arr[swap_l]
    
    rev_l = -1
    rev_r = -1
    for ind in range(len(arr) - 1):
        if rev_l == -1 and arr[ind] > arr[ind + 1]:
            rev_l = ind
        elif rev_l != -1 and arr[ind] < arr[ind + 1]:
            rev_r = ind
            break
    
    to_rev = arr[rev_l:rev_r+1]
    arr = arr[:rev_l] + to_rev[::-1] + arr[rev_r+1:]
    
    if is_sorted(arr):
        print("yes")
        print("reverse {} {}".format(rev_l + 1, rev_r + 1))
        return True
    
    print("no")
    return False

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    almostSorted(arr)
