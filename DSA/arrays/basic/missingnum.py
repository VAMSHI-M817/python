arr = [1, 2, 3, 4, 6, 7, 8]


def missingNum(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum


res = missingNum(arr)
print(res)
