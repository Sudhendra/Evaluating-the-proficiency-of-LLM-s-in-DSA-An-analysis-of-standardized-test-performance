class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]

            lo, hi = 1, n
            ans = n
            while lo <= hi:
                x = (lo + hi) // 2
                broken = dp(k-1, x-1)
                not_broken = dp(k, n-x)
                if broken > not_broken:
                    hi = x - 1
                    ans = min(ans, broken + 1)
                else:
                    lo = x + 1
                    ans = min(ans, not_broken + 1)

            memo[(k, n)] = ans
            return ans

        return dp(k, n)
