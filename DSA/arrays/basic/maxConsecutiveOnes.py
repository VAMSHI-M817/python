arr = [1, 2, 1, 1, 1, 4, 5, 1, 1, 4, 1, 1, 1, 1]


def maxConsecutiveOnes(arr):
    count = 0
    max_count = 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            count = 0
        if max_count < count:
            max_count = count
    return max_count


res = maxConsecutiveOnes(arr=arr)
print(res)
