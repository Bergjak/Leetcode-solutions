import collections
from math import comb
from bisect import bisect_left

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        nums = collections.Counter(nums)
        nums = sorted(nums.items())
        p = [0]
        n = len(nums)
        res = 0
        for i in range(n):
            p.append(p[-1] + nums[i][1])

        for r in range(n):
            v = nums[r][1]
            if 3 * nums[r][0] < target:
                res += v * (v - 1) * (v - 2) // 6

            right = nums[r][0]

            for l in range(r):
                if 2 * nums[r][0] + nums[l][0] < target:
                    res += comb(nums[r][1], 2) * nums[l][1]

                if nums[r][0] + 2 * nums[l][0] < target:
                    res += nums[r][1] * comb(nums[l][1], 2)

                left = nums[l][0]
                t = target - (left + right) - 1
                mid = bisect_left(nums, (t, 0))

                if l < mid and l + 1 < r:
                    if mid >= r:
                        mid = r - 1

                    while l < mid and left + nums[mid][0] + right >= target:
                        mid -= 1

                    if l >= mid:
                        continue

                    res += nums[r][1] * nums[l][1] * (p[mid + 1] - p[l + 1])
        return res