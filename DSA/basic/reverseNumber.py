def reverseNumber(number):
    revNum = 0
    while number > 0:
        lastdigit = number % 10
        revNum = (revNum * 10) + lastdigit
        number //= 10
    return revNum


res = reverseNumber(5612)
print(res)
