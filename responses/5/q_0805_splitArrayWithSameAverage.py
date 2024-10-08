from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        dp = [set() for _ in range(n//2 + 1)]
        dp[0].add(0)
        
        for num in nums:
            for i in range(n//2, 0, -1):
                for prev_sum in dp[i - 1]:
                    dp[i].add(prev_sum + num)
        
        for i in range(1, n//2 + 1):
            if total_sum * i % n == 0 and total_sum * i // n in dp[i]:
                return True
        
        return False
