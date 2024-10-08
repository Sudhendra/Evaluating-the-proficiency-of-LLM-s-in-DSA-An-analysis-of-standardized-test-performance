from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        
        for num in nums:
            if count == 0:
                majority = num
            count += 1 if num == majority else -1
        
        return majority
