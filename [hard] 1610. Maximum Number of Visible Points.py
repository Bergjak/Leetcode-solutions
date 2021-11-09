import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # So, we should figure out how the window of points we can view is a function of location and angle
        # Like, I think I should be able to slide a left pointer along the points and a right pointer that goes as far right as possible
        # for each left point while keeping the leftmost point in range of the rightmost point
        # Thus, the points should be sorted so that sliding rightward through the points has the same effect as rotating around a circle

        angles = []
        score = 0
        for i in range(len(points)):
            points[i][0] -= location[0]
            points[i][1] -= location[1]
            if points[i] == [0, 0]:
                score += 1  # We are standing on this point and so can see it no matter where we are looking
            else:
                angles.append(math.degrees(math.atan2(points[i][1], points[i][0])))

        angles.sort()
        angles.extend([360 + x for x in angles])  # Extend the array so that we can wrap around the circle
        left = res = 0

        for right in range(len(angles)):

            while abs(angles[right] - angles[left]) > angle:
                left += 1

            res = max(res, right - left + 1)

        return res + score