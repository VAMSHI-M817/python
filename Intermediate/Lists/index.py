"This code finds the largest number in a list using a for loop."

my_list = [3, 4, 6, 100, 887, 337, 10]
largest = my_list[0]
for i in my_list:
    if i >= largest:
        largest = i
print(largest)


# """ This code finds the largest number in a list using a for loop."""
# my_list = [-3, -4, -6, -100, -887, -337, -10]
# largest = my_list[0]
# for i in my_list:
#     if i >= largest:
#         largest = i
# print(largest)


""" This code finds the smallest number in a list using a for loop."""

my_list = [1.5, 3, 4, 6, 100, 887, 337, 10]
smallest = my_list[0]
for i in my_list:
    if i <= smallest:
        smallest = i
print(smallest)

""""""
arr = [1, 2, 3, 4, 5, 6]


for i in range(0, len(arr)):
    print(arr[i])
    if arr[i] == 4:
        print("Found 4, breaking the loop.")
        break
