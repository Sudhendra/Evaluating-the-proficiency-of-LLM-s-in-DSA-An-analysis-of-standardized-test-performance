from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))  # Sort the intervals by end points, then start points
        ans = 0
        p1 = p2 = -1
        
        for start, end in intervals:
            if start > p2:
                ans += 2
                p2 = end
                p1 = end - 1
            elif start > p1:
                ans += 1
                p1, p2 = p2, end
        
        return ans
