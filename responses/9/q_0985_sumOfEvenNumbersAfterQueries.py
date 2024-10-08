from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        total_sum = sum(x for x in nums if x % 2 == 0)
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                total_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                total_sum += nums[index]
            res.append(total_sum)
        
        return res
