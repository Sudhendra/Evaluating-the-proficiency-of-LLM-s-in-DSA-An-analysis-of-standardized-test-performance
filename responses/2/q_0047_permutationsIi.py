from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(remaining, path, res):
            if not remaining:
                res.append(path[:])
                return
            
            for i, num in enumerate(remaining):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                path.append(num)
                backtrack(remaining[:i] + remaining[i+1:], path, res)
                path.pop()
        
        nums.sort()
        res = []
        backtrack(nums, [], res)
        return res