import heapq

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        p = [0]
        for i in range(len(nums)):
            p.append(p[-1] + nums[i])

        # I think I should solve like finding best interval pair but then modify that solution so that it becomes the best interval trio
        # I think I do that in 2 passes, wherein on the first pass I get the best interval pairs up to each index i and then on the 2nd
        # pass I get the best interval to the right of those 2 intervals. So, the second pass is just a reapeat of the first pass, but instead
        # of making a heap, I use best_up_to_i as the heap, which was made on the first pass.

        heap = []
        intervals = []
        best_up_to_i = []
        best_score = best_pair_score = 0
        start = None

        for i in range(k, len(p)):
            intervals.append([i - k, i - 1, p[i] - p[i - k]])

        for l, r, score in intervals:
            while heap and l > heap[0][0]:
                _, score2, left = heapq.heappop(heap)
                if score2 > best_score:
                    best_score = score2
                    start = left

            heapq.heappush(heap, (r, score, l))
            if best_score + score > best_pair_score:
                best_pair_score = best_score + score
            if start is not None:
                best_up_to_i.append((r, best_pair_score, start, l))

        start = None
        best_score = best_pair_score = 0
        heapq.heapify(best_up_to_i)
        res = [-1, -1, -1]

        for l, r, score in intervals:
            while best_up_to_i and l > best_up_to_i[0][0]:
                _, score2, left, mid = heapq.heappop(best_up_to_i)
                if score2 > best_score:
                    best_score = score2
                    start = left
                    middle = mid

            if start is not None and best_score + score > best_pair_score:
                best_pair_score = best_score + score
                res = [start, middle, l]

        return res