from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))  # Sort intervals by end point then start point
        ans = 0
        p1, p2 = -1, -1
        
        for start, end in intervals:
            if start > p1:  # If current start is greater than the first previous element
                ans += 2
                p2 = end - 1
                p1 = end
            elif start > p2:  # If current start is greater than the second previous element
                ans += 1
                p2 = p1
                p1 = end
        
        return ans
