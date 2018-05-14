if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)
    
    print(max(list(filter(lambda a: a != first, arr))))
