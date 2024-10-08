from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes
        
        time_points = sorted(map(time_to_minutes, timePoints))
        
        min_diff = min((y - x) % (24 * 60) for x, y in zip(time_points, time_points[1:] + time_points[:1]))
        
        return min(min_diff, 24*60 - min_diff)
