from collections import defaultdict

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        best_right_for_each_left = defaultdict(int)
        for i, r in enumerate(ranges):
            if r == 0: continue
            LEFT = max(0, i - r)
            RIGHT = min(n, i + r)
            best_right_for_each_left[LEFT] = max(best_right_for_each_left[LEFT], RIGHT)

        for l, r in best_right_for_each_left.items():
            intervals.append([l, r])
            if [l, r] == [0, n]: return 1
        intervals.sort()

        far_right = 0
        included_intervals = []

        for l, r in intervals:
            if r <= far_right: continue

            far_right = r

            if len(included_intervals) > 1 and l <= included_intervals[-1][1] and l <= included_intervals[-2][1]:
                included_intervals.pop()

            included_intervals.append([l, r])

        for i in range(len(included_intervals) - 1):
            _, r1 = included_intervals[i]
            l2, _ = included_intervals[i + 1]
            if r1 < l2: return -1

        if included_intervals and included_intervals[-1][-1] < n: return -1
        return len(included_intervals) or -1