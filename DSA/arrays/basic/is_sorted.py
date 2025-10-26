arr = [64, 29, 21, 25, 87, 45, 67]


def is_sorted(arr):
    if not arr:
        return 0

    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            return False
        else:
            return True
    return None


print(is_sorted(arr))
