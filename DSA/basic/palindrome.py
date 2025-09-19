def reverseNumber(number):
    revNum = 0
    dup = number
    while number > 0:
        lastDigit = number % 10
        revNum = (revNum * 10) + lastDigit
        number = number // 10
    if revNum == dup:
        return True
    else:
        return False


res = reverseNumber(12211)
print(res)


name = "vamshi"
print(str(12345)[::-1])
