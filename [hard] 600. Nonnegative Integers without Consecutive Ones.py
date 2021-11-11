from functools import cache

class Solution:
    def findIntegers(self, n: int) -> int:
        # It looks like, anytime there are consecutive ones in x, then dfs(x) == fib(bit of highest consecutive one) + dfs(x % bit of highest consecutive one)
        # Whereby % I mean erasing all the bits after the highest consecutive one (inclusive)

        @cache
        def fib(x):
            if x <= 1:
                return 1
            return fib(x - 1) + fib(x - 2)

        def dfs(x):
            # Either x contains consecutive ones (if so, call fib) or it does not (if so, count it and call dfs(x - 1))
            if x <= 0:
                return 1

            power = 0

            for y in range(x.bit_length() - 1, -1, -1):
                if x & (3 << y) == 3 << y:
                    x &= ((1 << x.bit_length()) - 1) << (y + 1)
                    power = y + 1
                    break

            return dfs(x - 1) + fib(power)

        return dfs(n)