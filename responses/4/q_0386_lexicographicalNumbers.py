from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            if num > n:
                return
            result.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        for i in range(1, min(10, n + 1)):
            dfs(i)

        return result
