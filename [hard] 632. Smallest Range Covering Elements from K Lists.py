from bisect import bisect_left
import sys


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # So, if we squashed all of nums into a single list, then we could sort that massive list and
        # look at each minimum at a time. Then, for each minimum, we'd bisect each list in the collection of lists
        # to see where the minimum would be placed, and then we would take the largest thing to the right of where we bisect, ie,
        # if bisect gave idx, then we'd just look at row[idx]. So, we could look from a set of numbers and we also would halt
        # as soon as the next element in the priority queue was placed at the end of one of the lists, since then we cannot
        # have an upper bound, and so we are done looking.

        A = set()
        for x in nums:
            A.update(x)
        A = sorted(A, reverse=True)

        ans = []
        bisect_idx_is_not_end_of_a_row = True  # This is set to False once bisect_left returns len(row)
        best = sys.maxsize
        rbow = -sys.maxsize

        while A and bisect_idx_is_not_end_of_a_row:
            lbow = A.pop()
            for row in nums:
                idx = bisect_left(row, lbow)
                if idx == len(row):
                    bisect_idx_is_not_end_of_a_row = False
                    break

                rbow = max(rbow, row[idx])

            if bisect_idx_is_not_end_of_a_row and rbow - lbow < best:
                best = rbow - lbow
                ans = [lbow, rbow]

        return ans