class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        for k in range(1, n+1):
            target = n - (k * (k - 1) // 2)
            if target <= 0:
                break
            if target % k == 0:
                count += 1
        return count