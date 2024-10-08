from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr):
        max_time = -1
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour <= 23 and minute <= 59:
                time = hour * 60 + minute
                max_time = max(max_time, time)
        return "" if max_time == -1 else f"{max_time // 60:02d}:{max_time % 60:02d}"
