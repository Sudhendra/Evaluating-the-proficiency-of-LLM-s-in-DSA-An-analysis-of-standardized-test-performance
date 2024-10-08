class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        
        powers_of_two = [1] * n
        for i in range(1, n):
            powers_of_two[i] = (powers_of_two[i-1] * 2) % MOD
        
        result = 0
        for i in range(n):
            result = (result + (nums[i] - nums[n-i-1]) * powers_of_two[i]) % MOD
        
        return result
