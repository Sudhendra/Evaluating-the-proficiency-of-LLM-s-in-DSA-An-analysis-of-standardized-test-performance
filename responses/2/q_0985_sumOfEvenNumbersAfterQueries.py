from typing import List

class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        total_sum = sum(num for num in nums if num % 2 == 0)
        result = []
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                total_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                total_sum += nums[idx]
            result.append(total_sum)
        
        return result
