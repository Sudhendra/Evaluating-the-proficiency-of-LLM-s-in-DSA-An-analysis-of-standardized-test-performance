class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            elif curr < n:
                left = k + 1
            else:
                right = k - 1
        return right
