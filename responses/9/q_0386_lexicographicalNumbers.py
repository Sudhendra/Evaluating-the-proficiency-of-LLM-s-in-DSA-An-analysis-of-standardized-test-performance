from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            if num > n:
                return
            result.append(num)
            for i in range(10):
                if 10*num + i <= n:
                    dfs(10*num + i)

        for i in range(1, 10):
            dfs(i)

        return result
