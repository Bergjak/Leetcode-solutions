from functools import cache
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # So, I think you could write an algorithm that generates permutations of the array
        # and then backtracks on those permutations. So you'd continue with a permutation if
        # ((nums[i] + nums[i+1])**0.5).is_integer() and abandon if not

        # So, I think you would start the backtrack by having n options for the first entry
        # and then you'd have n-1 options for the second entry, and so on.
        # When you backtrack, you leave out the most recent entry as a possible contender

        # So, maybe you make n calls of the backtrack function, each call starting with a different element of nums
        # and then you do the same within the function, making n-1 calls for choosing the second element on each first function call

        self.score = 0
        n = len(nums)

        @cache
        def back(x, ops, prev_choices):
            ops = list(ops)
            prev_choices = list(prev_choices)

            if not ops:
                self.score += 1

            for i in range(len(ops)):
                if ((x + ops[i]) ** 0.5).is_integer():
                    back(ops[i], tuple(ops[:i] + ops[i + 1:]), tuple(prev_choices + [ops[i]]))

        for i in range(len(nums)):
            back(nums[i], tuple(nums[:i] + nums[i + 1:]), tuple([nums[i]]))

        return self.score