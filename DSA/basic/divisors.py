nums = 36


def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


# divisors(nums)

import math


def optimalDivisor(number):
    div = int(math.sqrt(number))
    res = []
    # print(div)
    for i in range(1, div + 1):
        # print(i)
        if number % i == 0:
            res.append(i)
            if i != number // i:
                res.append(number // i)
    return res


Res = optimalDivisor(36)
print(Res)
