"""
Write a Python program
that takes an old number and a new number
from the user. The program should replace
every occurrence of the old number in a predefined
list with the new number and print the updated list.
"""

list = [985, 568, 458, 789, 789]

old = int(input("Enter old number = "))
new = int(input("Enter new number = "))

for i in range(0, len(list)):
    if list[i] == old:
        list.remove(list[i])
        list.insert(i, new)

print(list)
