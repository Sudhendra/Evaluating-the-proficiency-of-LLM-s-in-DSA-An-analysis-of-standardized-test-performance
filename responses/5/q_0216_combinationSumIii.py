from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, k, path, res):
            if target == 0 and k == 0:
                res.append(path)
                return
            if k == 0 or target < 0:
                return
            for i in range(start, 10):
                backtrack(i+1, target-i, k-1, path+[i], res)
        
        res = []
        backtrack(1, n, k, [], res)
        return res
