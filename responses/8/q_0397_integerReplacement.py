class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n, cache):
            if n == 1:
                return 0
            if n in cache:
                return cache[n]
            if n % 2 == 0:
                cache[n] = 1 + helper(n // 2, cache)
            else:
                cache[n] = 1 + min(helper(n + 1, cache), helper(n - 1, cache))
            return cache[n]

        return helper(n, {})
