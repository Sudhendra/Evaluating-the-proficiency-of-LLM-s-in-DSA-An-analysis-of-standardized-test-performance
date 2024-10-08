from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove_count = 0

        for interval in intervals[1:]:
            if interval[0] < end:
                remove_count += 1
            else:
                end = interval[1]

        return remove_count
