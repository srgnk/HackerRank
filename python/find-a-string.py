def count_substring(string, sub_string):
    res = 0
    len_sub = len(sub_string)
    
    for i in range(len(string) - len_sub + 1):
        if string[i:i + len_sub] == sub_string:
            res += 1
        i += 1
        
    return res
        