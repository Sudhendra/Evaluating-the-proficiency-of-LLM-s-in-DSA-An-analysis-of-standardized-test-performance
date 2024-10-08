from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = {}
        res = 0
        
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        for num in num_count:
            if num + 1 in num_count:
                res = max(res, num_count[num] + num_count[num + 1])
        
        return res
