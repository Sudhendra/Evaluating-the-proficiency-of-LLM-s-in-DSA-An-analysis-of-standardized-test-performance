from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        min_diff = min((y - x) % (24 * 60) for x, y in zip(time, time[1:] + time[:1]))
        return min(min_diff, 24 * 60 - min_diff)