class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1  # n itself can be written as n
        i = 2
        while i * (i + 1) / 2 <= n:
            if (n - i * (i + 1) / 2) % i == 0:
                count += 1
            i += 1
        return count
