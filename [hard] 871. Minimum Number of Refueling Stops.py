import heapq
class Solution:
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        heap, refills, pos = [], 0, 0
        stations.append([target, 0])
        full_tank = tank
        for i in range(len(stations)):
            p, g = stations[i]

            if full_tank < p: return -1
            full_tank += g

            while heap and p > tank + pos:
                tank -= heapq.heappop(heap)
                refills += 1

            heapq.heappush(heap, -g)
            tank -= p - pos
            pos = p

        return refills