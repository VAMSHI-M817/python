"""
remove all even elements from list
"""

list = [12, 35, 46, 77, 88, 91, 24, 53, 66, 39]
even = []

i = 0
while i <= len(list) - 1:
    if list[i] % 2 == 0:
        even.append(list[i])
        list.remove(list[i])
    i = i + 1

print(f"Odd Numbers are  : {list}")
print(f"Even numbers are  : {even}")
