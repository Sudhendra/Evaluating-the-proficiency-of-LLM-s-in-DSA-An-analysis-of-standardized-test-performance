class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        num_zeroes = s.count('0')
        num_ones = 0
        min_flips = num_zeroes
        
        for i in range(n):
            if s[i] == '0':
                num_zeroes -= 1
            else:
                num_ones += 1
            min_flips = min(min_flips, num_zeroes + num_ones)
        
        return min_flips