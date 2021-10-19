import sys, bisect

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        '''
        So, the idea of this algorithm is to find the shortest subarrays with sum at least k, and we want to do it in O(n)
        time. Therefore, we cannot simply enumerate all subarrays. To this end, I generate all prefix sums, giving the
        array p. Then, I form a monotonically increasing stack filled with unique values, hence lines 27 and 28. Then, when the
        stack is not empty, I search the stack for the the value that is closest to x - k. If I find x - k in the stack,
        then I have x - (x - k) == k, and since x is a prefix sum and x - k is a prefix sum, x - (x - k) corresponds
        to the sum of the subarray A[i: j] where j is the index of x in p and i is the index of x - k. If we cannot
        get x - k in the stack, then we just do the closest possible value Y s.t. x - Y > k.
        '''


        p = [0]
        for i in range(len(nums)):
            p.append(p[-1] + nums[i])

        indices = {}
        stack = []
        ans = sys.maxsize

        for i, x in enumerate(p):

            while stack and stack[-1] >= x:
                stack.pop()

            if stack:
                idx = bisect.bisect_right(stack, x - k)
                if idx == 0:
                    left = stack[idx]
                elif idx == len(stack):
                    left = stack[idx - 1]
                else:
                    if x - stack[idx] >= k:
                        left = stack[idx]
                    elif x - stack[idx - 1] >= k:
                        left = stack[idx - 1]
                if x - left >= k:
                    ans = min(ans, i - indices[left])

            stack.append(x)
            indices[x] = i  # I think you'd always want the rightmost possible index

        return ans if ans != sys.maxsize else -1