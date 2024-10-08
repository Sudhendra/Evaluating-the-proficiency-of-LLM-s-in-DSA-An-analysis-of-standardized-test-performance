class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur: int, res: List[int]) -> None:
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                if 10*cur + i <= n:
                    dfs(10*cur + i, res)
        
        res = []
        for i in range(1, 10):
            dfs(i, res)
        
        return res