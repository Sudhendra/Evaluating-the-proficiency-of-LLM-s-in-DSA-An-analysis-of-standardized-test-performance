class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))  # Sort by ending points and then starting points

        result = 0
        p1 = p2 = -1

        for start, end in intervals:
            if start > p2:  # Current interval doesn't intersect with previous interval
                result += 2
                p2 = end
                p1 = end - 1
            elif start > p1:  # Current interval intersects with 1 element of previous interval
                result += 1
                p1 = p2
                p2 = end

        return result