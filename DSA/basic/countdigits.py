n = 123456789


def countDigits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1

    return count


res = countDigits(n)
print(res)
