class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Count number of 1s to the right of each position
        n = len(s)
        ones_to_right = [0] * n
        ones_to_right[n-1] = int(s[n-1] == '1')
        for i in range(n-2, -1, -1):
            ones_to_right[i] = ones_to_right[i+1] + int(s[i] == '1')

        # Determine minimum flips based on current position
        min_flips = ones_to_right[0]
        zeros_to_left = 0
        for i in range(n):
            if s[i] == '0':
                min_flips = min(min_flips, zeros_to_left + ones_to_right[i])
                zeros_to_left += 1

        return min_flips
