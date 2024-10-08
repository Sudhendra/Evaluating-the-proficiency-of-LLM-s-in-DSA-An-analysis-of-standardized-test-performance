class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000: # If n is too large, the probability is very close to 1
            return 1.0

        memo = {}
        def rec(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            memo[(a, b)] = 0.25 * (rec(a-100, b) + rec(a-75, b-25) + rec(a-50, b-50) + rec(a-25, b-75))
            return memo[(a, b)]

        return rec(n, n)