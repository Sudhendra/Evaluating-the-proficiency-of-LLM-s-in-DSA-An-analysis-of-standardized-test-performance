class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        for i in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                if curr >= n:
                    curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10
        return res
