class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        
        def check(base: int, length: int) -> bool:
            res = 0
            for _ in range(length):
                res = res * base + 1
            return res == n
        
        for m in range(math.floor(math.log(n, 2)), 1, -1):
            l, r = 2, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if check(mid, m):
                    return str(mid)
                elif check(mid, m) < n:
                    l = mid + 1
                else:
                    r = mid - 1
        return str(n - 1)
