from typing import List

class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []
        
        for val, index in queries:
            original_num = nums[index]
            nums[index] += val
            if original_num % 2 == 0:
                even_sum -= original_num
            
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            result.append(even_sum)
        
        return result
