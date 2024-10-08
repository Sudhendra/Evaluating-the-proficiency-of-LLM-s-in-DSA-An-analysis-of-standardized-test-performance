class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        for i in range(1, int((2 * n) ** 0.5) + 1):
            if (2 * n) % i == 0:
                if i % 2 == 1 or (2 * n) // i % 2 == 1:
                    count += 1
        return count
