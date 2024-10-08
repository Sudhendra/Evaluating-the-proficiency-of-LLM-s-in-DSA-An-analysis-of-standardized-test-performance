class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(n**0.5) + 1
        for m in range(max_m, 1, -1):
            k = int(n ** (1 / m))
            if k >= 2 and (k**(m+1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)
