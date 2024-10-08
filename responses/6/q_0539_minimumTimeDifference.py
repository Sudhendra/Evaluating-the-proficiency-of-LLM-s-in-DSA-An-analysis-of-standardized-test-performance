from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        timePoints.sort()

        minutes = [convert_to_minutes(time) for time in timePoints]
        min_diff = float('inf')

        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i+1] - minutes[i])

        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])  # Check circular difference

        return min_diff
