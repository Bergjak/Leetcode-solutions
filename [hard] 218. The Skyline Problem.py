import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        past_heights_and_right_bounds = []  # (height, right)
        lefts = []
        # So, I sort the buildings such that the largest heights come first, which is needed for the heap.
        # Notice that it's the case that we want the left corner of each highest (non-occluded) building.
        buildings.sort(key=lambda x: (x[0], -x[2]))

        for l, r, h in buildings:
            # I place the rights in the heap and then remove all buildings from the heap that are before the
            # left bound of the current building, since I will never interact with those buildings again.
            while past_heights_and_right_bounds and past_heights_and_right_bounds[0][1] < l:
                heapq.heappop(past_heights_and_right_bounds)

            # If the heap does not exist, or the height of the current building is larger than the height of the
            # tallest building in the heap, then we necessarily have a building whose left-bound is visible.
            if not past_heights_and_right_bounds or -past_heights_and_right_bounds[0][0] < h:
                lefts.append([l, h])

            heapq.heappush(past_heights_and_right_bounds, (-h, r))

        # Now, I walk along buildings from the right to the left.
        buildings.sort(key=lambda x: (x[1], x[2]), reverse=True)
        past_heights_and_left_bounds = []
        rights = []

        for l, r, h in buildings:
            while past_heights_and_left_bounds and past_heights_and_left_bounds[0][1] > r:
                heapq.heappop(past_heights_and_left_bounds)

            if not past_heights_and_left_bounds or -past_heights_and_left_bounds[0][0] < h:
                if not past_heights_and_left_bounds:
                    # There is no smaller height, so the best thing is the ground, hence H = 0.
                    H = 0
                else:
                    # We make this the height we append because it is the first height less than
                    # the height h of the current building, which is what we need for the answer.
                    H = -past_heights_and_left_bounds[0][0]
                rights.append([r, H])

            heapq.heappush(past_heights_and_left_bounds, (-h, l))

        return sorted(lefts + rights)