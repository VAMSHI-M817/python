def twoSum(arr, target):
    if not arr:
        return 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return None


print(twoSum([1, 2, 3, 4, 5, 6], 10))
