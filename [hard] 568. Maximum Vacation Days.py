class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        # So, we want to find the path through the graph with the largest sum of edges
        # So, I can go backwards from the final week.
        # So, approximately: for each j in days[j][-c-1] += max(days[i][-c] for i in range(n) if edge[i][j])
        n, k = len(days), len(days[0])
        edges = [[] for _ in range(n)]

        for i in range(n):
            edges[i].append(i)
            for j in range(n):
                if flights[i][j]:
                    edges[i].append(j)

        for i in range(k - 2, -1, -1):
            for j in range(n):
                vacation_days = 0
                for path in edges[j]:
                    vacation_days = max(vacation_days, days[path][i + 1])

                days[j][i] += vacation_days

        return max(days[i][0] for i in edges[0])