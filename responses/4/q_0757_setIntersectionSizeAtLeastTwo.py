from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))  # Sort intervals by ending point then starting point
        length = len(intervals)
        result = 0
        point1 = -1
        point2 = -1

        for start, end in intervals:
            if start > point1:  # If the current interval does not intersect with point1
                result += 2
                point2 = end - 1
                point1 = end
            elif start > point2:  # If the current interval does not intersect with point2
                result += 1
                point2 = point1
                point1 = end

        return result
