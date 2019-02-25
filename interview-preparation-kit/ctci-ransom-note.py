dict_mag = dict()
dict_ran = dict()

def ransom_note(magazine, ransom):
    for word in magazine:
        if word in dict_mag.keys():
            dict_mag[word] += 1
        else:
            dict_mag[word] = 1
    
    for word in ransom:
        if word in dict_ran.keys():
            dict_ran[word] += 1
        else:
            dict_ran[word] = 1

    for key in dict_ran.keys():
        if dict_ran[key] > dict_mag[key]:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
