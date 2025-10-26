arr = [64, 29, 21, 25, 87, 45, 67]


# O(n**2)
def largestNum(arr):
    largest = 0
    for i in range(len(arr)):
        for num in arr:
            if num > largest:
                largest = num
    return largest


print(largestNum(arr))


# O(n)
def largestNum(arr):
    largest = arr[0]
    for i in range(len(arr)):
        largest = max(largest, arr[i])

    return largest


print(largestNum(arr))
