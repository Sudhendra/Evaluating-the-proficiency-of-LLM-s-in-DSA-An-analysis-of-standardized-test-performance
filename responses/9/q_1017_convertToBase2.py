class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        res = ""
        while n != 0:
            remain = n % -2
            n //= -2
            if remain < 0:
                remain += 2
                n += 1
            res = str(remain) + res
        
        return res
