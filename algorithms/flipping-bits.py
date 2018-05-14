if __name__ == "__main__":
    T = int(input().strip())

    correct = 1 << 32

    for _ in range(T):
        num = int(input().strip())
        print(~num + correct)

