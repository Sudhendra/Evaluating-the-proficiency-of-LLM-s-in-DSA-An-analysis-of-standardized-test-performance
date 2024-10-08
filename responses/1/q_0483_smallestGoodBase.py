class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        max_m = int(num ** 0.6) + 1
        for m in range(max_m, 1, -1):
            k = int(num ** (1 / (m - 1)))
            if (k ** m - 1) // (k - 1) == num:
                return str(k)
        return str(num - 1)
