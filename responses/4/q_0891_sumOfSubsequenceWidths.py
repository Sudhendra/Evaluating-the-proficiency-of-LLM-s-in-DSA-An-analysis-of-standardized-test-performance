class Solution:
    
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power_of_two = [1] * n
        for i in range(1, n):
            power_of_two[i] = power_of_two[i - 1] * 2 % MOD
        
        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + nums[i] * (power_of_two[i] - power_of_two[n - i - 1])) % MOD
        
        return total_sum
