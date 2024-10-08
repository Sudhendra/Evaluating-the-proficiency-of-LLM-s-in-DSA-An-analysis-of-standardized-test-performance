class Solution:
    def countArrangement(self, n: int) -> int:
        def count_util(n, pos, visited, memo):
            if pos == n + 1:
                return 1

            key = (pos, visited)
            if key in memo:
                return memo[key]

            count = 0
            for i in range(1, n + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    count += count_util(n, pos + 1, visited, memo)
                    visited[i] = False

            memo[key] = count
            return count

        return count_util(n, 1, [False] * (n + 1), {})
