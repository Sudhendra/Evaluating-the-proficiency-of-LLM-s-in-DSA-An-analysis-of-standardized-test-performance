from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, k, n, path, res):
            if k == 0 and n == 0:
                res.append(path)
            for i in range(start, 10):
                if i > n:
                    break
                backtrack(i+1, k-1, n-i, path+[i], res)

        res = []
        backtrack(1, k, n, [], res)
        return res
