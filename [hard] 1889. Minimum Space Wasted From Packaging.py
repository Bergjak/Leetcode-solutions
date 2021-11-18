import sys
from itertools import accumulate
from bisect import bisect_right
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        # we can binary search on packages to see where the smallest box from each supplier can be placed
        # and we can quickly compute the cost from a prefix sum array by looking at the bisect idx from packages and then the cost is
        # (idx+1) * boxes[j][i] - prefix[idx] or something approximately like that (my indices may be wrong)
        # There are 10**5 entries in boxes at most and each search will cost log(len(packages)) time. So, that should be an n*log(m) time algo
        packages.sort()
        prefix = list(accumulate(packages))
        best_cost = sys.maxsize

        for j in range(len(boxes)):
            boxes[j].sort()
            if boxes[j][-1] < packages[-1]:
                continue

            cost = 0
            past_idx = -1

            for box_size in boxes[j]:
                idx = bisect_right(packages, box_size)
                if idx == past_idx:
                    continue

                current_selection = box_size * (idx) - prefix[idx - 1]

                if past_idx != -1:
                    past_selection = (box_size * (past_idx) - prefix[past_idx - 1])
                else:
                    past_selection = 0

                cost += current_selection - past_selection
                past_idx = idx

            best_cost = min(cost, best_cost)

        return best_cost % (10 ** 9 + 7) if best_cost < sys.maxsize else -1