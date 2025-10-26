"""
Oka number ki maximum two divisor undali means haa number
1 tho and own ga divisor avvali if incase more than
2 divisors unte adhi prime avvadu

what is prime number
A prime number is a natural number
greater than 1 that has exactly two distinct
positive divisors: 1 and itself.
"""

# n = 12


def PrimeNum(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if count > 2:
            return False
    return True


arr = [2, 3, 4, 5, 7, 9, 11, 12, 13, 15, 17, 19, 20]

for num in arr:
    res = PrimeNum(num)
    print(res)
