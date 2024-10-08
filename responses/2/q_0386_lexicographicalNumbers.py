class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(curr: int, result: List[int]) -> None:
            result.append(curr)
            for i in range(0, 10):
                next_num = 10 * curr + i
                if next_num <= n:
                    dfs(next_num, result)

        result = []
        for i in range(1, min(n + 1, 10)):
            dfs(i, result)
        
        return result