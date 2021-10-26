from itertools import combinations
from bisect import bisect_left
import sys

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        half = len(nums) // 2
        left, right = nums[:half], nums[half:]
        summ = sum(nums) / 2
        full_sum = 2 * summ
        res = sys.maxsize

        # So, we want to find **TWO ARRAYS OF LENGTH N** (I wasted a lot of time because I missed that requirement) that have
        # the smallest absolute difference. Thus, we just search over all possible combinations. To search over all possible combos,
        # we do some arithmetic: We want a length n subset x of nums that's disjoint from the other length n subset y.
        # So, notice that if we construct a length n subset array x, we get the second subset array y for free:
        # x = [nums[i], nums[k], ..., nums[c]] and so sum(y) = sum(nums) - sum(x). Then we are looking for min(abs(sum(y) - sum(x)))
        # but that's equal to min(abs(sum(nums) - 2*sum(x))). So, really what we are looking for is the best subset x of nums.
        # Therefore, we generate all possible length n subsets, taking the first k elements from the left half of nums
        # and the last n-k elements from the second half of nums. We do this because it's much cheaper than generating
        # all possible length n subsets of nums, which is naively 2**30 in the worst case.
        # Then, to actually do this search, we generate all possible length k sums from the left side of nums and then we sort
        # those sums in an array. Then, since the array is sorted, we can binary search on that array with sums from the right side
        # to find the best possible conjunctions of elements from left side and right side. The best possible conjunction
        # is if sum(nums) / 2 == sum_of_k_elements_from_left + sum_of_n-k_elements_from_right
        # and hence we bisect left_sums with sum(nums)/2 - r (returning idx) so that our left_sums[idx] + r ~= sum(nums) / 2 as desired.

        for k in range(1, half + 1):
            left_sums = set()
            for c_left in combinations(left, k):
                left_sums.add(sum(c_left))
            left_sums = sorted(left_sums)

            for c_right in combinations(right, half - k):
                r = sum(c_right)
                target = summ - r
                idx = bisect_left(left_sums, target)

                if idx > 0:
                    res = min(res, abs(full_sum - 2 * (left_sums[idx - 1] + r)))

                if idx < len(left_sums):
                    res = min(res, abs(full_sum - 2 * (left_sums[idx] + r)))

                if res == 0:
                    return 0

        return int(res)