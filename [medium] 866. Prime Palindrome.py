class Solution:
    def primePalindrome(self, n: int) -> int:
        if n == 1: return 2

        def factor(x):
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        # This is a generator function that returns palindromic numbers in sorted order
        def get_num():
            for l in range(8):
                for num in range(10 ** l, 10 ** (l + 1)):
                    s = str(num)
                    pal = s[:-1] + s[::-1]
                    yield int(pal)
                for num in range(10 ** l, 10 ** (l + 1)):
                    s = str(num)
                    pal = s + s[::-1]
                    yield int(pal)

        for num in get_num():
            if num < n or not factor(num): continue

            return num