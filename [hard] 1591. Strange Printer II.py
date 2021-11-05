import collections

class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        islands = {}
        m, n = len(grid), len(grid[0])

        # I am grabbing the rectangular region that captures the four most extreme coordinates of each color
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in islands:
                    islands[grid[i][j]] = [i, j, 0, 0]
                else:
                    islands[grid[i][j]][0] = min(islands[grid[i][j]][0], i)
                    islands[grid[i][j]][1] = min(islands[grid[i][j]][1], j)
                    islands[grid[i][j]][2] = max(islands[grid[i][j]][2], i)
                    islands[grid[i][j]][3] = max(islands[grid[i][j]][3], j)

        degree = collections.defaultdict(set)
        graph = collections.defaultdict(list)
        q = collections.deque()

        # Now, I am considering the degree of a color to be how many other colors are inside of its rectangle.
        for color, (x0, y0, x1, y1) in islands.items():
            for i in range(x0, x1 + 1):
                for j in range(y0, y1 + 1):
                    degree[color].add(grid[i][j])
            if color in degree[color]:
                degree[color].remove(color)
            if not degree[color]:
                q.append(color)
            for root in degree[color]:
                graph[root].append(color)

        # Now I am just topologically sorting
        while q:
            root = q.popleft()

            for node in graph[root]:
                degree[node].remove(root)
                if not degree[node]:
                    q.append(node)

        # If the topological sort was successful, then all of the colors have degree 0
        return all(x == set() for x in degree.values())