"""
A Function which calls itself until condition satisfy
is know as the recursion process
"""


def headRecursion(n):

    if n == 0:
        return

    headRecursion(n - 1)  # callsfirst
    print(n)  # after work


headRecursion(5)
