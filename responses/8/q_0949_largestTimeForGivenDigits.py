from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1

        for h1, h2, m1, m2 in permutations(arr):
            hour = 10 * h1 + h2
            minute = 10 * m1 + m2
            if hour < 24 and minute < 60:
                time = 60 * hour + minute
                max_time = max(max_time, time)

        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60) if max_time != -1 else ""
