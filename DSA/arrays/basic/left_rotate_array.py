arr = [64, 29, 21, 25, 87, 45, 67, 77]


def rotateArrayByOnePlace(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[len(arr) - 1] = temp
    return arr


print(rotateArrayByOnePlace(arr))
