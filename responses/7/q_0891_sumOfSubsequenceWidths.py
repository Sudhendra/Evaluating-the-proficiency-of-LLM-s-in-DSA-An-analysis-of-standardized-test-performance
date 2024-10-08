class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        max_powers = [1] * n
        for i in range(1, n):
            max_powers[i] = (max_powers[i - 1] * 2) % MOD
        
        total_width = 0
        for i in range(n):
            total_width = (total_width + (max_powers[i] - max_powers[n - i - 1]) * nums[i]) % MOD
        
        return total_width
