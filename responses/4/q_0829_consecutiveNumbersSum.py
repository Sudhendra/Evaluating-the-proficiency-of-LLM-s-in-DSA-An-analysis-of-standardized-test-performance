class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        num = 1

        while n > 0:
            if n % num == 0:
                count += 1
            n -= num
            num += 1
        
        return count
