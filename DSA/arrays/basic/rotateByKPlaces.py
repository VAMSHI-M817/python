arr = [64, 29, 21, 25, 87, 45, 67, 77]


def rotateByKPlaces(arr, k):
    k %= len(arr)
    print(k)
    temp = arr[0:k]
    res = []
    for i in range(k, len(arr)):
        res.append(arr[i])
    return res + temp


print(rotateByKPlaces(arr, 15))
