from itertools import permutations

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def overlap(s1, s2):
            max_len = min(len(s1), len(s2))
            for i in range(max_len - 1, -1, -1):
                if s1.endswith(s2[:i]):
                    return i
            return 0

        def combine(s1, s2):
            olap = overlap(s1, s2)
            return s1 + s2[olap:]

        n = len(words)
        dp = [[""] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = words[i]

        for mask in range(1 << n):
            for i in range(n):
                if not dp[mask][i]:
                    continue
                for j in range(n):
                    if mask & (1 << j) == 0:
                        new_str = combine(dp[mask][i], words[j])
                        if dp[mask | (1 << j)][j] == "" or len(new_str) < len(dp[mask | (1 << j)][j]):
                            dp[mask | (1 << j)][j] = new_str

        min_len = float('inf')
        ans_idx = 0
        for i in range(n):
            if len(dp[(1 << n) - 1][i]) < min_len:
                min_len = len(dp[(1 << n) - 1][i])
                ans_idx = i

        return dp[(1 << n) - 1][ans_idx]