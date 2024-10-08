from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        max_factors = [pow(2, i, mod) for i in range(n)]
        min_factors = [pow(2, n-i-1, mod) for i in range(n)]
        
        result = 0
        for i in range(n):
            result = (result + (max_factors[i] - min_factors[i]) * nums[i]) % mod
        
        return result
