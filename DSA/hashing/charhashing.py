def charHashing(n):
    s = [0] * 256
    for ch in n:
        s[ord(ch) - ord("a")] += 1
    return s


res = charHashing("ééééé")
# print(res)


# arr = [1, 2, 311, 4, 5, 6, 7, 8, 9]
# print(arr[311])


def countFreq(arrs, n):
    visited = [False] * n
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i + 1, n):
            if arrs[i] == arrs[j]:
                visited[j] = True
                count += 1
        print(
            f"{arrs[i]} - {count}",
        )


arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
countFreq(arr, n)
