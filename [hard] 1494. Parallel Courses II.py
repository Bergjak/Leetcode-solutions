from functools import cache
import itertools, math

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        if not relations: return int(math.ceil(n / k))

        needed = [0 for _ in range(n)]
        for u, v in relations:
            needed[v - 1] |= 1 << (u - 1)
        finished = (1 << n) - 1

        @cache
        def dp(mask):

            if mask == finished:
                return 0

            # ans is large so that we can abandon trajectories which do not reach the base case (mask == finished)
            ans = 100000

            # I could generate all size <= k combos of classes that I have not taken and then try all of those trajectories
            not_taken_and_can_take = []
            for i in range(n):
                if not mask & (1 << i) and needed[i] & mask == needed[i]:
                    not_taken_and_can_take.append(i)

            combos = []
            for combo_size in range(1, k + 1):
                combos.extend(itertools.combinations(not_taken_and_can_take, combo_size))

            for combo in combos:

                mask0 = mask
                for i in combo:
                    mask0 |= 1 << i

                ans = min(ans, dp(mask0) + 1)

            return ans

        return dp(0)