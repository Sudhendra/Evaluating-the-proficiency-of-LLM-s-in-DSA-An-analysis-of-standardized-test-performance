class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            divisor = factor*10
            count += (n//divisor)*factor + min(max(n%divisor - factor + 1, 0), factor)
            factor *= 10
        return count
