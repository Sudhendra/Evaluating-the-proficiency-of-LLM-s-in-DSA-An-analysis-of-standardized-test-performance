class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(start, visited):
            nonlocal count
            if start > n:
                count += 1
                return
            for i in range(1, n + 1):
                if not visited[i] and (i % start == 0 or start % i == 0):
                    visited[i] = True
                    backtrack(start + 1, visited)
                    visited[i] = False

        count = 0
        visited = [False] * (n + 1)
        backtrack(1, visited)
        return count
