from sortedcontainers import SortedList
import itertools
# A brute force solution would be, for each i < j, we count the number of p[j] - p[i] which fall in the range [lower, upper]
# We could just find the number below upper, the number below lower, and then return num_upper - num_lower
# I can do that in nlog(n) time by walking through nums and collecting elements in a sorted list, but before I add an element to the sorted list,
# I bisect that list to see how many elements are larger than p[i] (I want larger because I am taking p[j] - p[i] <= upper)
# And I think you do the bisection with (p[i] - upper)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p, lower = list(itertools.accumulate(nums)), lower - 1
        sl, n, res = SortedList(), len(p), 0

        for i in range(n):
            up = p[i] - upper
            below = p[i] - lower

            up_idx = i - sl.bisect_left(up)
            below_idx = i - sl.bisect_left(below)

            res += up_idx - below_idx + int(p[i] <= upper) - int(p[i] <= lower)

            sl.add(p[i])

        return res