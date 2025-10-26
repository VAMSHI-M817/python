arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]


def removeDuplicates(arr):
    if not arr:
        return 0

    i = 0
    for j in range(i + 1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


length = removeDuplicates(arr)
print(arr[:length])
