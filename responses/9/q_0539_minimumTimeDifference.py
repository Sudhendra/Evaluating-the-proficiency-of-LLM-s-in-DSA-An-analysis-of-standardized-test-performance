from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hour, minute = map(int, time_str.split(':'))
            return hour * 60 + minute

        timePoints = sorted(map(time_to_minutes, timePoints))
        min_diff = float('inf')

        for i in range(len(timePoints) - 1):
            diff = timePoints[i + 1] - timePoints[i]
            min_diff = min(min_diff, diff, 1440 - diff)

        return min_diff
