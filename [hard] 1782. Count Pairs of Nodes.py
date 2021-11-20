import sys
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        node_degree = [0] * (n + 1)
        graph = [set() for _ in range(n + 2)]
        overlap_counter = defaultdict(int)
        res, BIG = [], sys.maxsize

        for x, y in edges:
            node_degree[x] += 1
            node_degree[y] += 1
            graph[x].add(y)
            graph[y].add(x)
            overlap_counter[tuple(sorted([x, y]))] += 1

        # We make a sorted list of the degrees (i.e., the incidence) of each node so that we can perform binary search on this list
        # which will vastly speed up our queries
        incidences = []
        for node, solo_incidence in enumerate(node_degree):
            incidences.append((solo_incidence, node))
        incidences.sort()
        m = len(incidences)

        for query in queries:
            # Now, we bisect right our sorted incidences list with the query. Every node to the right of the index (inclusive) has a large enough incidence such that
            # it can form an incidence pair with all other n-1 nodes. So, that means we can count all of the possible pairs from these large nodes by a counting formula,
            # which is what we use to initialize "ans", the integer that we will append to res, the array we return.
            idx = bisect_right(incidences,(query, BIG))  # BIG is just so we can do bisection_right on a list of tuples
            nodes_we_counted_but_that_have_too_large_overlap = set()

            # So, the first node (incidences[idx][1]) can pair with all other n-1 nodes in the list. The same goes for incidences[idx+1][1] but to avoid counting the overlap
            # (ie, we do not want to count the pair (incidences[idx][1], incidences[idx+1][1]) again), we have to subtract 1 from n-1, giving n-2. And then we continue this
            # all the way until reaching m-1. So, we have the formula to initialize ans as:
            # n-1 + (n-2) + (n-3) + ... + (n - (m - idx)) == n * (m - idx) - sum(x for x in range(1, m-idx+1)) == n * (m - idx) - (m-idx)*(m-idx+1)//2
            ans = n * (m - idx) - (m - idx) * (m - idx + 1) // 2

            # Now we have to count node pairs (x, y) such that node_degree[y] is not large enough alone to pair with anything else to surpass the query threshold.
            # So, what we do first is assume there does not exist any overlap (i.e., x and y sharing z edges to eachother) at all between nodes, which means we
            # will likely be over counting. So, we then have to look at all the nodes which could possibly have had too large an overlap to allow the pair to pass
            # the threshold. But the only such nodes are the one in the edge set of incidences[right][1], and so we check if the pair is large enought to cross
            # the query threshold and so have been counted and then we check to see if the overlap is too large to be legally counted. To avoid duplicate subtractions,
            # we collect the bad pairs inside of a set, and then we subtract the size of that set from ans. Then we append ans to res. We then repeat for all of the queries.
            for right in range(idx - 1, 0, -1):
                left = bisect_right(incidences, (query - incidences[right][0], BIG))

                if right > left:
                    ans += right - left

                    for node in graph[incidences[right][1]]:
                        was_counted = node_degree[node] + incidences[right][0] > query
                        possible_overlap = tuple(sorted([incidences[right][1], node]))
                        should_not_be_counted = node_degree[node] + incidences[right][0] - overlap_counter[possible_overlap] <= query

                        if was_counted and should_not_be_counted:
                            nodes_we_counted_but_that_have_too_large_overlap.add(possible_overlap)

            res.append(ans - len(nodes_we_counted_but_that_have_too_large_overlap))

        return res