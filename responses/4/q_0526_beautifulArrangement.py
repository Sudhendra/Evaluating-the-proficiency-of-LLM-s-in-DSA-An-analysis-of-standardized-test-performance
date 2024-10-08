class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(idx, selected, visited):
            if idx == n + 1:
                return 1

            count = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % idx == 0 or idx % i == 0):
                    visited[i] = True
                    count += dfs(idx + 1, selected + 1, visited)
                    visited[i] = False

            return count

        return dfs(1, 0, [False] * (n + 1))
