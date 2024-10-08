class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power_of_two = [1] * n
        for i in range(1, n):
            power_of_two[i] = (power_of_two[i-1] * 2) % MOD
        
        result = 0
        for i in range(n):
            result = (result + (power_of_two[i] - power_of_two[n-i-1]) * nums[i]) % MOD
        
        return result
