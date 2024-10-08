class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(curr: int, result: List[int]) -> None:
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                if 10 * curr + i <= n:
                    dfs(10 * curr + i, result)

        result = []
        for i in range(1, min(n, 10)):
            dfs(i, result)
        return result
