class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(curr: int, res: List[int]) -> None:
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                if 10 * curr + i <= n:
                    dfs(10 * curr + i, res)
        
        result = []
        for i in range(1, 10):
            dfs(i, result)
        
        return result