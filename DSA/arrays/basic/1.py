class BasicArray:
    def __init__(self, arr):
        self.arr = arr

    # FIND FIRST NON REPEAT ELEMENT IN ARRAY
    # method2
    # res = set() with res.add(num)
    def problem1(self):
        arr = self.arr
        res = []
        for num in arr:
            if num in res:
                break
            res.append(num)
        return num

    # Find the first non-repeating element in array
    def problem2(self):
        arr = self.arr
        n = len(arr)
        freq = {}
        for ele in arr:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        for ele in arr:
            if freq[ele] == 1:
                return ele
        return None

    # Find the element that appears only once (when others appear twice)
    def problem3(self):
        arr = self.arr
        n = len(arr)
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1
            if count > 1:
                return arr[i]

    # Find the missing number from a sequence 1 to N
    def problem4(self):
        arr = self.arr
        n = len(arr) + 1

        total = n * (n + 1) // 2
        return total - sum(arr)


# res = BasicArray([3, 78, 45, 45, 6, 9, 12])
res = BasicArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14])

print(res.problem4())
