from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_in_minutes = []
        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            time_in_minutes.append(hours * 60 + minutes)

        time_in_minutes.sort()

        min_diff = float('inf')
        for i in range(1, len(time_in_minutes)):
            min_diff = min(min_diff, time_in_minutes[i] - time_in_minutes[i - 1])

        min_diff = min(min_diff, 24*60 - (time_in_minutes[-1] - time_in_minutes[0]))

        return min_diff
