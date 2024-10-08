from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        result = 0
        
        for i in range(firstLen - 1, n):
            max_sum1 = prefix_sum[i+1] - prefix_sum[i+1-firstLen]
            max_sum2 = max(prefix_sum[j+1] - prefix_sum[j+1-secondLen] for j in range(i - secondLen, i - firstLen + 1))
            result = max(result, max_sum1 + max_sum2)
            
        for i in range(secondLen - 1, n):
            max_sum1 = prefix_sum[i+1] - prefix_sum[i+1-secondLen]
            max_sum2 = max(prefix_sum[j+1] - prefix_sum[j+1-firstLen] for j in range(i - firstLen, i - secondLen + 1))
            result = max(result, max_sum1 + max_sum2)
        
        return result
