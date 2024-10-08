class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = []
        while n != 0:
            remainder = n % 2
            res.append(str(remainder))
            n = -(n // 2)
        return ''.join(res[::-1])
