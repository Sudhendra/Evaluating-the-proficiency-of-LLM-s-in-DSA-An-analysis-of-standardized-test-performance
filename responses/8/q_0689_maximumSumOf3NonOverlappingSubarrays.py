from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum_nums = [0]
        for num in nums:
            sum_nums.append(sum_nums[-1] + num)
        
        max_sum = 0
        max_sum_indexes = []
        
        for i in range(k, n - 2 * k + 1):
            for j in range(i + k, n - k + 1):
                for l in range(j + k, n - k + 1):
                    sum_window = sum_nums[i + k] - sum_nums[i] + sum_nums[j + k] - sum_nums[j] + sum_nums[l + k] - sum_nums[l]
                    if sum_window > max_sum:
                        max_sum = sum_window
                        max_sum_indexes = [i, j, l]
        
        return max_sum_indexes
