arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]


# def sec(left,right):
#     res = []
#     i=j=0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             if len(res) == 0 or left[i] != res[-1]:
#                 res.append(left[i])
#                 i +=1
#         else:
#             if len(res) == 0 or left[j] != res[-1]:
#                 res.append(right[j])
#             j+=1

#     res.extend(left[i:])
#     res.extend(right[j:])

#     return res
# print((sec(arr1,arr2)))


def func(nums1, nums2):
    result = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            if nums1[i] != 0:
                result.append(nums1[i])
            i += 1
        else:
            if nums2[j] != 0:
                result.append(nums2[j])
            j += 1
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result


print(func(arr1, arr2))
