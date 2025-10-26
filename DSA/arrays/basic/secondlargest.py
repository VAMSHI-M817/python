arr = [64, 29, 21, 25, 87, 45, 67, 77]


def secondLargest(arr):
    for _ in range(len(arr)):
        largest = max(arr)
        secondLargest = 0
        for j in range(len(arr)):
            if arr[j] < largest and arr[j] > secondLargest:
                secondLargest = arr[j]
    return secondLargest


print(secondLargest(arr))
