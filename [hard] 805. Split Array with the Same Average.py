from itertools import combinations

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # So, if we take a combo of size k, then the other half is (numSum - x) / (n - k)
        # So, notice that it would suffice to look at all size 1 subsets, size 2 subsets, ... size n//2 subsets
        # and then each time check if (numSum - subset_sum) / (n - len(subset)) == subset_sum / len(subset)
        # Then, in the worst case, we would be looking at (30 choose 15) different subsets.
        # But notice in that case, we are doing the problem of Partition Array into Two Arrays of Length n
        # So, I should be able to generalize that approach for reducing the complexity

        numSum = sum(nums)
        n = len(nums)
        half = n // 2
        left, right = nums[:half], nums[half:]

        for subset_size in range(1, len(nums)):
            target = numSum * subset_size / n
            # We have target equal to this because, if we have answer, then we have some subsequence X of nums
            # such that (nums - sum(X)) / (n - len(X)) == sum(X) / len(X). But searching over all subsets naively
            # would be too slow. Therefore, I split the search for X into looking for a left half and a right half
            # of the subsequence X. So, we can say X = L + R, where L is some subsequence of the left half of nums
            # and R is some subsequence of the right half of nums s.t. len(R) + len(L) == subset_size. Then we have
            # the equation (nums - (L + R)) / (n - subset_size) == subset_size / (L + R) which can be transformed
            # into L + R == sum(nums) * subset_size / n and therefore we look for L == sum(nums) * subset_size / n - R

            for k in range(1, subset_size + 1):
                left_sums = set()

                for c_left in combinations(left, k):
                    left_sums.add(sum(c_left))

                for c_right in combinations(right, subset_size - k):
                    find = target - sum(c_right)

                    if find in left_sums:
                        return True
        return False