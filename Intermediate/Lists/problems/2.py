"""
Write a Python program that asks the user to enter
the number of elements they want in a list, then
takes that many integer inputs from the user and stores
them in a list. Finally, print the complete list.
"""

length = int(input("Enter List Length : "))
arr = []
for i in range(1, length + 1):
    num = int(input("Enter a num : "))
    arr.append(num)

print("Final Answer : ", arr)
