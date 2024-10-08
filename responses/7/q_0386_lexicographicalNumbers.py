class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(curr, n, result):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                if 10 * curr + i <= n:
                    dfs(10 * curr + i, n, result)
        
        result = []
        for i in range(1, 10):
            dfs(i, n, result)
        
        return result
