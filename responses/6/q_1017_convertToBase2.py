class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'

        res = ''
        while n != 0:
            r = n % 2
            n = -(n // 2)
            if r < 0:
                r += 2
                n += 1
            res = str(r) + res

        return res
