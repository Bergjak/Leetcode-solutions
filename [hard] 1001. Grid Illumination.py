from collections import defaultdict
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        d0, d1, rows, cols = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        lamps = {(x, y) for x, y in lamps}
        for y, x in lamps:
            r0 = n - 1 - max(x, y)
            r1 = min(x, n - 1 - y)
            d0[(x + r0, y + r0)] += 1
            d1[(x - r1, y + r1)] += 1
            cols[x] += 1
            rows[y] += 1

        ans = []
        for y, x in queries:
            r0 = n - 1 - max(x, y)
            r1 = min(x, n - 1 - y)
            if d1[(x - r1, y + r1)] > 0 or d0[(x + r0, y + r0)] > 0 or cols[x] > 0 or rows[y] > 0:
                ans.append(1)
            else:
                ans.append(0)

            for u, v in [(x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1),
                         (x - 1, y + 1), (x, y), (x, y + 1)]:
                if (v, u) in lamps:
                    r0 = n - 1 - max(u, v)
                    r1 = min(u, n - 1 - v)
                    lamps.remove((v, u))
                    d0[(u + r0, v + r0)] -= 1
                    d1[(u - r1, v + r1)] -= 1
                    cols[u] -= 1
                    rows[v] -= 1

        return ans