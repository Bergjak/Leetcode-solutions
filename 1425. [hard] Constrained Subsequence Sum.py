import sys
import collections
'''
So, the objective is to get the maximum subsequence sum (in an array including negative elements) wherein elements
(nums[i], nums[j]) in the maximum subsequence sum are such that i < j and j - i <= k. So, if we had the best 
subsequence sum for the last k indices (that is, the answers for nums[:i - k], nums[:i-k+1], ..., nums[:i])
then the answer for nums[:i+1] = max(max(answers for nums[:i - k], nums[:i-k+1], ..., nums[:i]) + nums[i], nums[i]).
Thus, the problem reduces to finding the (maximum entry in the window of size k of the previous k answers) X and then
choosing ans(nums[:i+1]) = max(nums[i], X + nums[i]). So, I implement a function for generating the maximum window
and I take the sum as appropriate, all while checking if the most recent sum is largest or not. Finally, I return
the largest possible sum.
'''


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        d = collections.deque()
        res = -sys.maxsize

        for i, x in enumerate(nums):
            if d and i - d[0][0] - k > 0:
                d.popleft()

            if d and d[0][1] > 0:
                dp_i = d[0][1] + x
            else:
                dp_i = x

            while d and d[-1][1] <= dp_i:
                d.pop()

            if res < dp_i:
                res = dp_i

            d.append([i, dp_i])

        return res
