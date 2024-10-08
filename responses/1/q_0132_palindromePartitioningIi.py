class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False]*n for _ in range(n)]
        cuts = [0] * n

        for end in range(n):
            min_cuts = end
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 1 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True
                    min_cuts = 0 if start == 0 else min(min_cuts, cuts[start - 1] + 1)
            cuts[end] = min_cuts

        return cuts[n - 1]