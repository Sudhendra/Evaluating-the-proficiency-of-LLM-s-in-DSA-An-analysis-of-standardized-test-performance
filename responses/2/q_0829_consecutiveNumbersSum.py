class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upper_limit = int((2 * n + 0.25)**0.5 - 0.5) + 1

        for k in range(1, upper_limit):
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1

        return count