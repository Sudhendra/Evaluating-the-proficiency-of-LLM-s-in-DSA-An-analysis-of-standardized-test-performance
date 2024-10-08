class Solution:
    
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        x = 1
        while n - x >= 1:
            x *= 2
        return n ^ (x - 1)
