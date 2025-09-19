"""i to n using head recursion"""


def parameterizedRecursion(i, n):

    if i > n:
        return

    print(i)
    parameterizedRecursion(i + 1, n)


# parameterizedRecursion(1, 20)

"""i to n using tail recursion"""


def parameterizedRecursion(i, n):

    if i > n:
        return

    parameterizedRecursion(i, n - 1)
    print(n)


# parameterizedRecursion(1, 20)

"""n to i using head recursion"""


def tailRecursion1(n, i):

    if i > n:
        return

    print(n)
    tailRecursion1(i, n - 1)


# tailRecursion1(20, 1)


"""n to i using tail recursion"""


def tailRecursion2(i, n):

    if i > n:
        return

    tailRecursion2(i + 1, n)
    print(i)


# tailRecursion2(1, 20)


sum = 0


def sumOfNum(sum, i, n):
    if i > n:
        print(sum)
        return
    sumOfNum(sum + i, i + 1, n)


sumOfNum(sum, 1, 20)
