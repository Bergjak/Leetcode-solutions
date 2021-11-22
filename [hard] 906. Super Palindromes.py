class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)

        def get_num():
            for l in range(30):
                for i in range(10 ** l, 10 ** (l + 1)):
                    s = str(i)
                    pal = s[:-1] + s[::-1]
                    yield int(pal)
                for i in range(10 ** l, 10 ** (l + 1)):
                    s = str(i)
                    pal = s + s[::-1]
                    yield int(pal)

        res = 0
        for num in get_num():
            if num ** 2 < left: continue
            if num ** 2 > right: return res
            new_num = num ** 2
            new_num = str(int(new_num))
            if new_num == new_num[::-1]:
                res += 1