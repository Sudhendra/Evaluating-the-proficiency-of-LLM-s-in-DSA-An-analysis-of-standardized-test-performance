from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for p in permutations(arr):
            h = p[0] * 10 + p[1]
            m = p[2] * 10 + p[3]
            if 0 <= h < 24 and 0 <= m < 60:
                time = h * 60 + m
                max_time = max(max_time, time)
        
        if max_time == -1:
            return ""
        
        return f"{max_time // 60:02d}:{max_time % 60:02d}"
