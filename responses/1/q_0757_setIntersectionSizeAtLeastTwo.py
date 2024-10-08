class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))  # sort the intervals based on end points and then start points
        points = [-1, -1]  # initialize with two -1 to represent the last two points in containing set
        count = 0
        
        for interval in intervals:
            start, end = interval
            if start > points[1]:  # interval does not overlap with the last two points
                points = [end - 1, end]  # choose two points (end-1, end) in the interval
                count += 2
            elif start > points[0]:  # interval overlaps with one point, so choose end point and a non-shared point
                points = [points[1], end]  # choose two points with only end point common with previous set
                count += 1
                
        return count