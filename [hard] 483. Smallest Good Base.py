from math import log
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # So, we are solving for lowest base x s.t. x^k + x^(k-1) + ... + x^2 + x + 1 == n
        # Thus, base n-1 will always work, since n-1 + 1 == n
        # We want f(x, k) = x^k + x^(k-1) + ... + x^2 + x + 1 == n
        # Notice that f(x, k) = 1 + x(f(x, k-1)) and f(x, k - 1) == f(x, k) - x**k. So, f(x, k) = 1 + x(f(x,k) - x**k) and we want f(x, k) = n.
        # Therefore, we have that n = 1 + x(n - x**k) which implies that n * (1 - x) == 1 - x**k which implies that n = (1 - x**k)//(1 - x), as required.

        # Notice that f(x, k) for fixed k is monotonically increasing with x and same for fixed x and and increasing k.
        # So, perhaps we could do 2D binary search? Like, for each k we propose, we find the closest x. Or, since k will never
        # be bigger than 60 (ie, 2**60 > 10**18), we could just search for the best base x for each k and then return the lowest x that works
        # So, that's O(log(n)^2), i.e., log(n) for linear search over all possible k values and log(n) for binary searching for x
        # So, we will binary search over x-values until we find the integer x s.t. (1-x**(k+1))/(1-x) is closest to n as possible
        n = int(n)
        best = n-1
        for k in range(2, int(log(n, 2)) + 1):
            l, r = 1, n-1
            while l + 1 < r:
                mid = (l + r)//2
                f = (1 - mid**(k+1))//(1-mid)
                if f < n: l = mid
                elif f > n: r = mid
                else: return str(mid)
        return str(best)
