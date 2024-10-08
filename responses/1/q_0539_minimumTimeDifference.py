from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        min_diff = min((y - x) % (24 * 60) for x, y in zip(time_points, time_points[1:] + time_points[:1]))
        return min_diff
