class SortingMethods:
    def __init__(self, arr):
        self.arr = arr

    def selectionSort(self):
        arr = self.arr
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
        return arr

    def bubbleSort(self):
        arr = self.arr
        n = len(arr)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr

    def insertionSort(self):
        arr = self.arr
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def mergeSort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr

        n = len(arr)
        mid = n // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < (len(right)):

            if left[i] < right[j]:

                result.append(left[i])
                i += 1

            else:

                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


res = SortingMethods([64, 29, 21, 25, 87, 45, 67])


# print(res.selectionSort())
# print(res.bubbleSort())
# print("Insertion : ", res.insertionSort())
print("Merge : ", res.mergeSort())


if __name__ != "__main__":
    print("hello")
