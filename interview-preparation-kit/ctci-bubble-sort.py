n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bub_sort(arr, n):
    num_swaps = 0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > a[j+1]:
                buff = arr[j+1]
                arr[j+1] = a[j]
                a[j] = buff
                num_swaps += 1
    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))

bub_sort(a, n)