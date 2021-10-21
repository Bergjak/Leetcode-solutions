import sys
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        got = {k: False for k in needed.keys()}
        quantity_needed = len(got)
        left = 0
        LEFT = RIGHT = 0
        best = sys.maxsize

        for r in range(len(s)):

            if s[r] in needed:

                needed[s[r]] -= 1
                if needed[s[r]] == 0:
                    quantity_needed -= 1

                if needed[s[r]] <= 0:
                    while left < r:
                        if s[left] in needed:
                            if needed[s[left]] >= 0:
                                break
                            needed[s[left]] += 1

                        left += 1

                if quantity_needed <= 0 and r - left + 1 < best:
                    best = r - left + 1
                    LEFT = left
                    RIGHT = r + 1

        return s[LEFT: RIGHT]