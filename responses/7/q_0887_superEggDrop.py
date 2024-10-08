class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(k: int, n: int) -> int:
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]

            lo, hi = 1, n
            result = n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                if broken > not_broken:
                    hi = mid - 1
                    result = min(result, broken + 1)
                else:
                    lo = mid + 1
                    result = min(result, not_broken + 1)

            memo[(k, n)] = result
            return result

        return dp(k, n)
