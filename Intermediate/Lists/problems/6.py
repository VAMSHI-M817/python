"""
print list in reverse by copying main list inputs of 5 from users
"""

list = []

for i in range(0, 5):
    user = int(input("ent a num : "))
    list.append(user)

new_list = []
for i in range(len(list) - 1, -1, -1):
    new_list.append(list[i])

print(new_list)


"""
Average on numbers
"""
numbers = [10, 20, 30, 40, 50]
sum = 0
total = 0

for num in numbers:
    sum += num
    total += 1
print(f"average of nums : {sum/total}")
