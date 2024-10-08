class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        mul = 1
        while mul <= n:
            a = n // mul
            b = n % mul
            count += (a + 8) // 10 * mul + (a % 10 == 1) * (b + 1)
            mul *= 10
        return count