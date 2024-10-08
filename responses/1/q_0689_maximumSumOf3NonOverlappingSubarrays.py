from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0] * (n - k + 1)
        sums[0] = sum(nums[:k])
        
        for i in range(1, n - k + 1):
            sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]
        
        left, right = [0] * (n - k + 1), [0] * (n - k + 1)
        
        best = 0
        for i in range(1, n - k + 1):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        
        best = n - k
        for i in range(n - k - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best
        
        max_sum = 0
        result = []
        for j in range(k, n - 2 * k + 1):
            l, r = left[j-k], right[j+k]
            total = sums[l] + sums[j] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, j, r]
        
        return result
