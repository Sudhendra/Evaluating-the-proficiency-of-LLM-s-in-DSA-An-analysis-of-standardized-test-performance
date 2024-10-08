class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))

        for m in range(m_max, 1, -1):
            k = int(n ** (1/m))
            if k >= 2:
                if (k**(m+1)-1)//(k-1) == n:
                    return str(k)
        return str(n-1)