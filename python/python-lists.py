if __name__ == '__main__':
    N = int(input())
    outlist = []
    for _ in range(N):
        args = input().strip().split(' ')
        cmd = args[0]
        if cmd == 'insert':
            outlist.insert(int(args[1]), int(args[2]))
        elif cmd == 'remove':
            outlist.remove(int(args[1]))
        elif cmd == 'append':
            outlist.append(int(args[1]))
        elif cmd == 'print':
            print(outlist)
        elif cmd == 'sort':
            outlist.sort()
        elif cmd == 'pop':
            outlist.pop()
        elif cmd == 'reverse':
            outlist.reverse()
        
        
            
