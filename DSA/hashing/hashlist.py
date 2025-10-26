arr = [1, 2, 3, 4, 4, 3, 2, 1]

n = len(arr)
count = 0
s = 3
for i in arr:
    if s == i:
        count += 1

# print(count)


def hashlist(n):
    list = [1, 2, 3, 4, 4, 2, 2, 1, 1, 2, 2, 2]
    hasharr = [0] * (max(list) + 1)

    for num in list:
        if num == n:
            hasharr[n] += 1
    return max(hasharr)


print(hashlist(2))
