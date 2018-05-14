#!/usr/bin/env python3

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        a, b = input().strip().split(' ')
        
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code: {}".format(e))
        except ValueError as e:
            print("Error Code: {}".format(e))
            