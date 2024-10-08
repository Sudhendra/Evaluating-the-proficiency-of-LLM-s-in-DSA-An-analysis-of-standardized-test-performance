from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k, n, start, path, res):
            if k == 0 and n == 0:
                res.append(path[:])
                return
            if k == 0 or n == 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(k-1, n-i, i+1, path, res)
                path.pop()
                
        res = []
        backtrack(k, n, 1, [], res)
        
        return res
