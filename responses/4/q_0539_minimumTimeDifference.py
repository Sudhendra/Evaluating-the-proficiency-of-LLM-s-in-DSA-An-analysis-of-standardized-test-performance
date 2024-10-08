from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time: str) -> int:
            hh, mm = map(int, time.split(':'))
            return hh * 60 + mm

        time_points_in_minutes = sorted(map(time_to_minutes, timePoints))
        min_diff = min((b - a) % (24 * 60) for a, b in zip(time_points_in_minutes, time_points_in_minutes[1:] + time_points_in_minutes[:1]))
        
        return min_diff