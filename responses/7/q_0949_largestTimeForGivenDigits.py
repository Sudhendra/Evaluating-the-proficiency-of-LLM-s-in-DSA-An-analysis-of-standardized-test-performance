from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for p in permutations(arr):
            h = p[0]*10 + p[1]
            m = p[2]*10 + p[3]
            if h < 24 and m < 60:
                current_time = h*60 + m
                max_time = max(max_time, current_time)
        
        if max_time == -1:
            return ""
        else:
            max_hour = max_time // 60
            max_minute = max_time % 60
            return f"{max_hour:02d}:{max_minute:02d}"
