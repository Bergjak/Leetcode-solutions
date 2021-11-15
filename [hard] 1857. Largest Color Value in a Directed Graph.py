from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges: return 1
        # If a node has x in-going edges, then that node needs to look at all the prior nodes to get the max frequency of each color
        # on those preceding paths
        all_colors, n = set(colors), len(colors)

        graph, indegree, frequency = [], [], []
        for i in range(n):
            graph.append([])
            indegree.append(0)
            frequency.append(defaultdict(int, {colors[i]: 1}))

        for x, y in edges:
            if x == y: return -1
            graph[x].append(y)
            indegree[y] += 1

        visited = set()  # If you encounter a node in the visited set, then return -1, since that means there exists a cycle
        max_frequency = 0
        stack = []
        for node, degree in enumerate(indegree):
            if degree == 0:
                stack.append((node))

        while stack:
            node = stack.pop()

            for vertex in graph[node]:

                indegree[vertex] -= 1
                if indegree[vertex] == 0:
                    if vertex in visited:
                        return -1
                    visited.add(vertex)
                    stack.append(vertex)

                for color in all_colors:
                    frequency[vertex][color] = max(frequency[vertex][color], frequency[node][color] + int(color == colors[vertex]))
                    max_frequency = max(max_frequency, frequency[vertex][color])

        return max_frequency if set(indegree) == {0} else -1