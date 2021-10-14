from heapq import heappop, heappush
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # We have a 2500 sized input in worst case so we can do an O((mn)^2) algo
        # We need to first grab all of the integers larger than 1
        # and we should grab them with their coordinates and sort them (number, (i, j))
        # Then, from (0, 0), we head to the first tree, and then to second, etc.
        # There should be an optimal path from each tree to tree + 1 and therefore as soon as we hit the next tree,
        # I think we can delete all other paths from the queue, just taking the best path
        # So, we do BFS to get from tree_n to tree_n+1. Basically just iterative BFS with clearing queue per iteration.
        trees = []
        m, n = len(forest), len(forest[0])

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
        trees.sort()
        goal = 0  # This will be the pointer that we increment upon hitting trees[goal]
        end_tree = len(trees)  # Once goal equals this, then we are done
        ans = 0  # Upon hitting tree_k, dump your number of steps into this
        stack = [(0, 0, 0)]  # Steps taken, row, column
        visited = set()  # We also clear this out after every iteration

        while stack and goal < end_tree:

            while stack:
                steps, r, c = heappop(stack)
                if forest[r][c] == trees[goal]:
                    goal += 1
                    ans += steps
                    stack = [(0, r, c)]
                    visited.clear()
                    break

                for u, v in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= u < m and 0 <= v < n and forest[r][c] and (u, v) not in visited:
                        visited.add((u, v))
                        heappush(stack, (steps + 1, u, v))

        return ans if goal == end_tree else -1