class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(count, pos, visited):
            if pos == n + 1:
                nonlocal result
                result += 1
                return

            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    backtrack(count + 1, pos + 1, visited)
                    visited[i] = False

        result = 0
        visited = [False] * (n + 1)
        backtrack(0, 1, visited)
        return result