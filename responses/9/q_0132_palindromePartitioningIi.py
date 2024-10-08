class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        min_cuts = [0] * n

        for i in range(n):
            min_cuts[i] = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 1 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    if j > 0:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j - 1] + 1)
                    else:
                        min_cuts[i] = 0

        return min_cuts[n - 1]
