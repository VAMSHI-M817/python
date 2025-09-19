"""
A Function which calls itself until condition satisfy
is know as the recursion process
"""


def headRecursion(n):

    if n == 0:
        return

    print(n)  # calls first
    headRecursion(n - 1)  # calls after work


headRecursion(5)
