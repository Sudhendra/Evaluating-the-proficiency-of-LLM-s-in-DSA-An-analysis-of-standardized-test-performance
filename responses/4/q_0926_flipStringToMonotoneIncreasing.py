class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # Count number of ones before and including each index
        ones = [0] * (n + 1)
        for i in range(n):
            ones[i+1] = ones[i] + int(s[i])
        
        min_flips = float('inf')
        for i in range(n+1):
            flips = ones[i] + (n - i) - (ones[n] - ones[i])
            min_flips = min(min_flips, flips)
        
        return min_flips
