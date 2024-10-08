from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time: str) -> int:
            hh, mm = time.split(":")
            return int(hh) * 60 + int(mm)
        
        time_points_in_minutes = [convert_to_minutes(time) for time in timePoints]
        time_points_in_minutes.sort()
        
        min_diff = float("inf")
        for i in range(len(time_points_in_minutes) - 1):
            min_diff = min(min_diff, time_points_in_minutes[i+1] - time_points_in_minutes[i])
        
        min_diff = min(min_diff, 1440 + time_points_in_minutes[0] - time_points_in_minutes[-1])
        
        return min_diff
