class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        multiplier = 1
        while n >= multiplier:
            count += (n // (multiplier * 10)) * multiplier + min(max(n % (multiplier * 10) - multiplier + 1, 0), multiplier)
            multiplier *= 10
        return count
