from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                new_time = hour * 60 + minute
                if new_time > max_time:
                    max_time = new_time
                    max_hour, max_minute = hour, minute
        return f"{max_hour:02d}:{max_minute:02d}" if max_time != -1 else ""
