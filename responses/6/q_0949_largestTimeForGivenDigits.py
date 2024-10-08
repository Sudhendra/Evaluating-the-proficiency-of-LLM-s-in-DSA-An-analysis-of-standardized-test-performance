from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                curr_time = hour * 60 + minute
                max_time = max(max_time, curr_time)
        
        if max_time == -1:
            return ""
        else:
            return f"{max_time // 60:02d}:{max_time % 60:02d}"
