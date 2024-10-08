from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        valid_times = set()
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                valid_times.add(f"{h1}{h2}:{m1}{m2}")
        
        if not valid_times:
            return ""
        
        return max(valid_times)
