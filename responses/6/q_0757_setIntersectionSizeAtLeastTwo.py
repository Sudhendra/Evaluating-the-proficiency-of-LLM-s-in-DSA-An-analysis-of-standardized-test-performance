from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        n = len(intervals)
        count = 0
        points = []
        
        for start, end in intervals:
            if all(start > point or point > end for point in points):
                points.extend([end - 1, end])
                count += 2
            elif start < points[-1]:
                points.append(end)
                count += 1
        
        return count
