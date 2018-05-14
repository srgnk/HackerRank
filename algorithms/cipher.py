#!/bin/python3

import sys

def cipher(k, s):
    s_len = len(s)
    out_len = s_len - k + 1
    result = [0] * out_len
    
    result[-1] = int(s[-1])
    keep_prev = result[-1]
    for it_ind in range(1, out_len):
        # keep the result string only
        to_update = out_len - 1 - it_ind
        result[to_update] = int(s[-(it_ind+1)])
        #print(result)
        #print("it_ind = {} < {} = k".format(it_ind, k))
        #if it_ind < k:
        #    keep_prev = 0
        #    for k_ind in range(1, k):
        #        from_update = to_update + k_ind
        #        if from_update == out_len:
        #            #print('breaking')
        #            break
        #        #print("to_update = [{}] <-- [{}] outlen = {}".format(to_update, from_update, out_len))
        #        #result[to_update] ^= result[from_update]
        #        #print("POPULATE KEEP to_update = [{}] <-- [{}] outlen = {}".format(to_update, from_update, out_len))
        #        keep_prev ^= result[from_update]
        #else:
        #    #print("UPDATE KEEP to_update + k = [{} + {}]".format(to_update, k))
        #    keep_prev ^= result[to_update + k]
        if it_ind >= k:
            keep_prev ^= result[to_update + k]
            
        result[to_update] ^= keep_prev
        keep_prev ^= result[to_update]
                

    return "".join(map(str, result))
        
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    s = input().strip()
    result = cipher(k, s)
    print(result)
