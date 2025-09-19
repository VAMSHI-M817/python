"""
A number is an Armstrong
number if the sum of its
own digits raised to the
power of the number of
digits equals the number itself.
"""


def armStrong(number):
    original = number
    result = 0
    k = len(str(number))
    while number > 0:
        lastDigit = number % 10
        sum = lastDigit**k
        result += sum
        number = number // 10
    return result == original


res = armStrong(12345)
print(res)
