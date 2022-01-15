from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], T: int) -> int:
        r, c = len(matrix), len(matrix[0])
        res = -float('inf')

        psa = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                psa[i + 1][j + 1] = psa[i + 1][j] + psa[i][j + 1] - psa[i][j] + matrix[i][j]

        for i in range(1, r + 1):
            for k in range(1, i + 1):
                # So, I could have a third loop that makes each possible right side of the rectangle and then
                # do a binary search for the best possible left side of the rectangle.
                left_sides = SortedList()
                for j in range(1, c + 1):
                    right_side = psa[i][j] - psa[i - k][j]
                    target = right_side - T
                    idx = left_sides.bisect_left(target)

                    if idx < len(left_sides) and res < right_side - left_sides[idx] <= T:
                        res = right_side - left_sides[idx]
                    if idx > 0 and res < right_side - left_sides[idx - 1] <= T:
                        res = right_side - left_sides[idx - 1]
                    if res < right_side <= T:
                        res = right_side

                    if res == T:
                        return T

                    left_sides.add(right_side)

        return res