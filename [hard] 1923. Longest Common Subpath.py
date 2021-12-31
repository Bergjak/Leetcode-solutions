MOD = 1_000_000_000_001

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        paths.sort(key=len)
        m = len(paths[-1])
        BASE = n

        POW = [1] * (m + 1)
        for i in range(m):
            POW[i + 1] = BASE * POW[i] % MOD

        hash_arrays = []
        for path in paths:
            hash_arrays.append([0] * (len(path) + 1))
            for i in range(len(hash_arrays[-1]) - 1):
                hash_arrays[-1][i + 1] = (hash_arrays[-1][i] * BASE + path[i]) % MOD

        def isCommon(size):
            hash_set = set()
            for j in range(len(hash_arrays[0]) - size):
                hash_set.add((hash_arrays[0][j + size] - hash_arrays[0][j] * POW[size]) % MOD)

            for i in range(1, len(hash_arrays)):
                new_hash_set = set()
                for j in range(len(hash_arrays[i]) - size):
                    new_hash_set.add((hash_arrays[i][j + size] - hash_arrays[i][j] * POW[size]) % MOD)

                hash_set &= new_hash_set

                # This is the case if we have no matching hash_keys
                if not hash_set:
                    return False
            return True

        left, right = -1, len(paths[0]) + 1
        ans = 0
        while left + 1 < right:
            mid = (left + right) // 2

            if isCommon(mid):
                ans = max(ans, mid)
                left = mid
            else:
                right = mid

        return ans