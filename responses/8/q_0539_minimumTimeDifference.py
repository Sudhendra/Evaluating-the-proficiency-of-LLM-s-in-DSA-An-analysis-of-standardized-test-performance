from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points_minutes = []
        for time in timePoints:
            hours, minutes = map(int, time.split(":"))
            time_points_minutes.append(hours * 60 + minutes)

        time_points_minutes.sort()
        
        min_diff = float('inf')
        for i in range(1, len(time_points_minutes)):
            min_diff = min(min_diff, time_points_minutes[i] - time_points_minutes[i - 1])
        
        min_diff = min(min_diff, 1440 + time_points_minutes[0] - time_points_minutes[-1])  # Consider difference between first and last time

        return min_diff
