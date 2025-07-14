"""
how many numbers are divisible by 7 from 1 to 100
"""

count = 0
i = 1
while i <= 100:
    if i * 7 <= 100:
        count = count + 1
    i = i + 1
# print(f"The total count div by 7 : {count}")


"""
Print numbers that are divisible by 7 from 1 to 100
"""

i = 1
nums = []
while i <= 100:
    if i % 7 == 0:
        nums.append(i)
    i = i + 1

# print(f"Numbers that are divisible by 7 from 1 to 100 ==> {nums}")

"""
Print numbers that are divisible by 6 and 7 from 1 to 200
"""

i = 1
arr = []
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        arr.append(i)
    i = i + 1
# print(arr)


i = 1
count = 0
while i <= 200:
    if i % 6 <= 0 and i % 7 <= 0:
        count = count + 1
    i = i + 1
print(count)
