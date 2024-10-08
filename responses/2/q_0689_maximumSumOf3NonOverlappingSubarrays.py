from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        max_sum = 0
        left_intervals = []
        for i in range(k, n-2*k+1):
            left_sum = prefix_sum[i] - prefix_sum[i-k]
            if left_sum > max_sum:
                max_sum = left_sum
                left_intervals = [i-k+1]
            
        right_intervals = []
        for j in range(n-2*k, k-1, -1):
            right_sum = prefix_sum[j+2*k] - prefix_sum[j+k]
            if right_sum >= max_sum:
                max_sum = right_sum
                right_intervals = [j]
        
        max_intervals = []
        for m in range(k, n-k+1):
            mid_sum = prefix_sum[m+k] - prefix_sum[m]
            if left_intervals and right_intervals and mid_sum + max_sum > left_sum + right_sum:
                max_intervals = left_intervals + [m] + right_intervals
        
        return max_intervals
