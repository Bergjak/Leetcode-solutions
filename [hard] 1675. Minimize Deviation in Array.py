import heapq
import sys

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # I am visualizing the problem as fixed length intervals of varying heights, and the height of each interval can discretely shift its height.
        # I need to find the height which that has the minimum maximum difference between other heights in the array.
        # So, an O(n^2*log(n)) solution would be to get every possible height of each entry and then find the closest hight of every other entry
        # to this height.  That solution will be too slow.
        heights = set()
        max_height = 0
        for x in nums:
            if x % 2 != 0:
                heights.add((x, 2 * x))
            else:
                OG = x
                while x % 2 == 0:
                    x //= 2
                heights.add((x, OG))
            max_height = max(max_height, x)

        heights = list(heights)
        heapq.heapify(heights)
        res = sys.maxsize

        # What if I just treat heights as a heap, and I just keep increasing the minimum and comparing it against the current maximum, and
        # I return the minimum(max(heights) - min(heights)) for each configuration of the heap

        while True:
            l, r = heapq.heappop(heights)
            if l < r:
                L = 2 * l
            else:
                return res
            max_height = max(max_height, L)
            heapq.heappush(heights, (L, r))
            res = min(res, max_height - heights[0][0])