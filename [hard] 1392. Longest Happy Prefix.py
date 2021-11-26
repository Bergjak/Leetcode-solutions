class Solution:
    def longestPrefix(self, s: str) -> str:
        # I could just treat the alphabet as a base 26 number system and then do
        # prefix and suffix comparisons, and then just take the best. If I use a big integer
        # to modulo the numbers, I can keep numbers small enough and have very low odds of collision
        # (ie, very low odds of getting a false positive).

        pre, suf = 0, 0
        n = len(s)
        ans = 0
        HASH = 10 ** 9 + 7

        for i in range(n - 1):
            pre_num = ord(s[i]) - 97
            suf_num = ord(s[~i]) - 97
            pre = (pre * 26 + pre_num) % HASH
            suf = (suf_num * (pow(26, i, HASH)) + suf) % HASH

            if pre == suf:
                ans = i + 1

        return s[:ans]