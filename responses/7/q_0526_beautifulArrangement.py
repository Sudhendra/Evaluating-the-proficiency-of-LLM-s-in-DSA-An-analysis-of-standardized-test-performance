class Solution:
    def countArrangement(self, n: int) -> int:
        def countArrangements(pos, visited, n):
            if pos == 0:
                return 1

            result = 0
            for i in range(1, n+1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    result += countArrangements(pos - 1, visited, n)
                    visited[i] = False
            return result

        visited = [False] * (n+1)
        return countArrangements(n, visited, n)
