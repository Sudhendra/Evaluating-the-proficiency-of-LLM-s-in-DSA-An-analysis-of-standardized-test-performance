from itertools import permutations

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def overlap(w1, w2):
            max_overlap = 0
            for i in range(min(len(w1), len(w2)), 0, -1):
                if w1.endswith(w2[:i]):
                    return i
            return max_overlap

        N = len(words)
        dp = [['' for _ in range(N)] for _ in range(1<<N)]

        for mask in range(1<<N):
            for i in range(N):
                if not (mask & (1 << i)):
                    for j in range(N):
                        if mask & (1 << j):
                            overlap_len = overlap(dp[mask ^ (1 << i)][j], words[i])
                            if dp[mask][i] < dp[mask ^ (1 << i)][j] + words[i][overlap_len:]:
                                dp[mask][i] = dp[mask ^ (1 << i)][j] + words[i][overlap_len:]

        superstring = min(dp[-1], key=len)
        return superstring
