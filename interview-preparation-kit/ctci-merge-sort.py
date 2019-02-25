import sys

def countInversions(array):
    cnt_inv = 0

    if len(array) <= 1:
        return array, 0

    ar_left, inv_left = countInversions(array[:int(len(array)/2)])
    ar_right, inv_right = countInversions(array[int(len(array)/2):])

    ar_merged = []
    i = j = 0
    len_left = len(ar_left)
    len_right = len(ar_right)
    
    for k in range(len(array) - 1):
        if i == len_left or j == len_right:
            break

        if ar_left[i] <= ar_right[j]:
            ar_merged.append(ar_left[i])
            i += 1
        else:
            ar_merged.append(ar_right[j])
            j += 1
            cnt_inv += len_left - i

    ar_merged += ar_left[i:]
    ar_merged += ar_right[j:]
    return ar_merged, cnt_inv + inv_left + inv_right


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        arr_sorted, result = countInversions(arr)
        print(result)