class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])  # Sort the intervals based on the end points
        
        count = 1  # Count of non-overlapping intervals
        end = intervals[0][1]  # End point of the current interval
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]
        
        return len(intervals) - count