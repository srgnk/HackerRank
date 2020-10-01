def mini_game(s):
    S_length = len(s)
    player1, player2 = 0,0
    
    for i in range(S_length):
        if s[i] in "AEIOU":
            player1 += S_length - i
        else:
            player2 += S_length - i        
    print(S_length)        
    if player1 > player2:
        return "s",player1
    elif player1 < player2:
        return "k ",player2
    else:
        print ("Draw")
    print(player2)    
s='AEIOU'

print(mini_game(s))
