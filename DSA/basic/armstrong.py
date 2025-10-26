"""
A number is an Armstrong
number if the sum of its
own digits raised to the
power of the number of
digits equals the number itself.
"""


def armStrong(number):
    og = number
    k = len(str(number))
    res = 0
    while number > 0:
        lastdigit = number % 10
        sum = lastdigit**k
        res += sum
        number //= 10
    return res == og


res = armStrong(930284)
print(res)
