import math
import string

def number_needed(a, b):
    result = 0
    a_dict = dict.fromkeys(string.ascii_lowercase, 0)
    b_dict = dict.fromkeys(string.ascii_lowercase, 0)
    
    for a_symb in a:
        a_dict[a_symb] = a_dict[a_symb] + 1
        
    for b_symb in b:
        b_dict[b_symb] = b_dict[b_symb] + 1
        
    #print(a_dict)
    #print(b_dict)
    
    for key in string.ascii_lowercase:
        result += math.fabs(a_dict[key] - b_dict[key])

    return int(result)

a = input().strip()
b = input().strip()

print(number_needed(a, b))
