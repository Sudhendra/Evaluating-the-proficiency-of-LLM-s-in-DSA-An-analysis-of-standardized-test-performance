class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        dp = {}

        def solve(i, remaining):
            if remaining == 0:
                return 0
            if remaining == 1:
                return 1 if i > 0 else 2

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            quotient = remaining // x
            remainder = remaining % x
            res = 0

            res = min(
                remainder * i + solve(i + 1, quotient),
                (x - remainder) * i + solve(i + 1, quotient + 1)
            )

            dp[(i, remaining)] = res
            return res

        return solve(0, target) - 1
