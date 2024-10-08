from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = 0
        p1 = -1
        p2 = -1

        for start, end in intervals:
            if start > p1:
                result += 2
                p2 = end
                p1 = end - 1
            elif start > p2:
                result += 1
                p2 = p1
                p1 = end
        return result
