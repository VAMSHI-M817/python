# """
# The GCD of two (or more) numbers is the
# largest positive integer that divides all
# of them without leaving a remainder.
# """

# import math


class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def GreatestCommonDivisor(self):
        gcd = []
        res = f" {(self.a,self.b)} GCD is : "
        for i in range(1, min(self.a, self.b) + 1):
            if self.a % i == 0 and self.b % i == 0:
                gcd.append(i)
        return res, max(gcd)

    def optimalGCD(self):
        a = self.a
        b = self.b
        while b != 0:
            temp = b
            b = a % b
            a = temp
            # print(a, b)
        return a


results = GCD(258, 196)
print(results.GreatestCommonDivisor())
print(results.optimalGCD())
