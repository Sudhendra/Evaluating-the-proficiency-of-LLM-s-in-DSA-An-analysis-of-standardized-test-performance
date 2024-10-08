from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        left, right = 0, 0
        min_len = float('inf')
        cur_sum = 0
        
        while right < n:
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        
        return min_len if min_len != float('inf') else 0
