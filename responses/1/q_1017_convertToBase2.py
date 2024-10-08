class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        res = []
        while n != 0:
            res.append(str(n & 1))
            n = -(n >> 1)
        
        return "".join(res[::-1])
