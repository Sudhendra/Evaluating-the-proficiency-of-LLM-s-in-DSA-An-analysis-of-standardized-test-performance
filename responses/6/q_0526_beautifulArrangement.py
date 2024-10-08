class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(position, visited):
            if position == n+1:
                return 1

            total = 0
            for num in range(1, n+1):
                if not visited[num] and (num % position == 0 or position % num == 0):
                    visited[num] = True
                    total += backtrack(position+1, visited)
                    visited[num] = False

            return total

        return backtrack(1, [False] * (n+1))
