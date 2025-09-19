"""
remove dups from a list using membership ops
"""

a = [16, 19, 25, 28, 1, 4, 7, 7, 7, 7, 77, 77, 7, 77, 6, 66, 6, 6, 6, 6, 10, 13]
new_list = []

for i in range(len(a) - 1, -1, -1):
    if a[i] not in new_list:
        new_list.append(a[i])
new_list.sort()
print(new_list)


""" 
printing index of user input
"""
a = [16, 19, 25, 28, 1, 4, 7, 7, 7, 7, 77, 77, 7, 77, 6, 66, 6, 6, 6, 6, 10, 13]

user = int(input("ent a num : "))

if user in a:
    print(a.index(user))
else:
    print(-1)
