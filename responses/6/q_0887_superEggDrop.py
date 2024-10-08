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

            low, high = 1, n
            min_moves = n
            while low <= high:
                mid = (low + high) // 2
                breaks = dp(k - 1, mid - 1)
                not_breaks = dp(k, n - mid)

                if breaks > not_breaks:
                    high = mid - 1
                    min_moves = min(min_moves, breaks + 1)
                else:
                    low = mid + 1
                    min_moves = min(min_moves, not_breaks + 1)

            memo[(k, n)] = min_moves
            return min_moves

        return dp(k, n)
