from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(num, n):
            if n == 0:
                return [num]
            res = []
            for next_num in {num % 10 + k, num % 10 - k}:
                if 0 <= next_num < 10:
                    res.extend([num * 10 + next_num for num in dfs(next_num, n - 1)])
            return res

        if n == 1:
            return list(range(10))
        
        res = []
        for num in range(1, 10):
            res.extend(dfs(num, n - 1))
        
        return res