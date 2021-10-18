from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], dt: int, change: int) -> int:
        '''
        If we have a 1D graph (ie, a straight line of nodes) then the answer will always be the time taken to walk
        to node n, walk back to n - 1 and back to n.

        If we do not have a 1D graph, then we still have to consider the above path as a contender. However, that should be
        the only contending path for which we revisit a node. Reasoning: The path i ==> i+1 ==> i ==> i+1 takes the same amount of time
        regardless of which node i.

        Therefore, I think we can do dijkstras with (time, node) (where (time, node) will also be the visited set entry), and
        when the first path is finished, compute the additional time taken for the cycle described above, and get the second
        completed path (the node right after the first completed path). Then sort these three options and return the second one.

        If time // change is odd, then stop. Else, go. Stopping just incurs a time penalty of change, and then we still go anyway
        '''

        visited = set()
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        qHeap = [(0, 1)]  # time (t), node
        finished = set()
        freq = defaultdict(int)

        while qHeap:
            t, node = heappop(qHeap)

            if node == n:
                finished.add(t)

                if len(finished) == 2:
                    return max(finished)

            stop_cost = t // change % 2
            if stop_cost:
                # t should now become the first multiple of change that is larger than t. t = change * (t//change + 1)
                t = change * (t // change + 1)

            for v in graph[node]:
                # We can filter by frequency less than 2 because we should never have to visit a node more
                # than twice, since we are looking for the second minimum time
                if (t + dt, v) not in visited and (v != node or (v == n - 1 and node == n)) and freq[v] < 2:
                    visited.add((t + dt, v))
                    freq[v] += 1
                    heappush(qHeap, (t + dt, v))