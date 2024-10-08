class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(perm, idx):
            nonlocal count
            if idx == n + 1:
                count += 1
                return
            for i in range(1, n + 1):
                if not visited[i] and (i % idx == 0 or idx % i == 0):
                    visited[i] = True
                    perm[idx] = i
                    backtrack(perm, idx + 1)
                    visited[i] = False
                    
        count = 0
        visited = [False] * (n + 1)
        perm = [0] * (n + 1)
        backtrack(perm, 1)
        return count
