arr = [0, 0, 0, 1, 2, 0, 0, 3, 3, 0, 4, 4, 6, 6]
arr = [1, 0, 0, 0, 2, 0, 0, 3, 3, 0, 4, 4, 6, 6]
arr = [1, 0, 0, 0, 2, 0, 0, 3, 3, 0, 4, 4, 6, 6]
arr = [1, 2, 3, 3, 0, 0, 0, 0, 0, 0, 4, 4, 6, 6]


def moveZeroes(arr):
    if not arr:
        return 0
    l = 0
    for r in range(len(arr)):
        if arr[r] == 0:
            continue
        else:
            temp = arr[r]
            arr[r] = arr[l]
            arr[l] = temp
            l += 1
    return arr


length = moveZeroes(arr)
print(length)
