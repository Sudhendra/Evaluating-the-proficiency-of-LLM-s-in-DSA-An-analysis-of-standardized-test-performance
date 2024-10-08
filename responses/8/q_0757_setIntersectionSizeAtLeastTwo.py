from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        intersection_size = 2
        last_point = [intervals[0][1] - 1, intervals[0][1]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > last_point[1]:
                intersection_size += 2
                last_point = [end - 1, end]
            elif start > last_point[0]:
                intersection_size += 1
                last_point = [last_point[1], end]
        
        return intersection_size
