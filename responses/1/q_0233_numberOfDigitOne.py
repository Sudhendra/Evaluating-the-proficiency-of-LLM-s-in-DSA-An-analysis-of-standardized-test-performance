class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        for i in range(1, n+1):
            count += str(i).count('1')

        return count