from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1
        
        result = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        backtrack([], counter)
        
        return result
