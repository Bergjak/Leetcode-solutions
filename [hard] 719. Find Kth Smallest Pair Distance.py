class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        n = len(nums)

        def isPossible(attempted_diff):
            left = smaller_diff_count = 0
            # Since nums is sorted, we can do the verification with 2 pointers, wherein we count how many differences are less
            # than attempted_diff. So, if nums[right] - nums[left] > attempted_diff: left += 1
            # and then right - left is how many differences are less than attempted_diff for those 2 pointers.

            for right in range(n):

                while left < right and nums[right] - nums[left] > attempted_diff:
                    left += 1

                smaller_diff_count += right - left
                if smaller_diff_count >= k:
                    return True
            return False

        while l < r:
            mid = (l + r) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        return l