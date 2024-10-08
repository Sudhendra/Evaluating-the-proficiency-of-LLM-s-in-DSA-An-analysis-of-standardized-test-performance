from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(31):  # Since 10^9 < 2^31, we only need to consider 31 bits
            count_ones = 0
            for num in nums:
                count_ones += (num >> i) & 1
            
            ans += count_ones * (n - count_ones)
        
        return ans
