from collections import deque
class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        # We could binary search our day number: l = 1, r = len(cells)
        # mid would then be the day we update to in the array cells

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mat = [[0] * n for _ in range(m)]

        def search(idx):
            visited = set()
            q = deque([(0, i) for i in range(n) if mat[0][i] == 0])

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    if 0 <= r + dr < m and 0 <= c + dc < n and mat[r + dr][c + dc] != 1 and (
                    r + dr, c + dc) not in visited:
                        visited.add((r + dr, c + dc))
                        if r + dr == m - 1: return True  # This is the case if we reached the bottom of the matrix
                        q.append((r + dr, c + dc))
            return False

        old_mid = 0
        l = 0
        r = len(cells)

        # I think I will end up returning l
        while l + 1 < r:
            mid = (l + r) // 2

            if old_mid < mid:  # we have to sink islands from cells[old_mid: mid+1]
                for idx in range(old_mid, mid):
                    u, v = cells[idx]
                    mat[u - 1][v - 1] = 1
            else:
                for idx in range(old_mid - 1, mid - 1, -1):
                    u, v = cells[idx]
                    mat[u - 1][v - 1] = 0

            search_result = search(mid)

            if search_result:  # This is the case if updating matrix up to cells[mid] still allows for reaching bottom of grid
                l = mid
            else:
                r = mid

            old_mid = mid

        return l
