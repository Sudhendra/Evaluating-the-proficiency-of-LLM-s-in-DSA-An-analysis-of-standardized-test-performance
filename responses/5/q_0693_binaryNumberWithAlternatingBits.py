class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = n & 1
        n >>= 1
        
        while n:
            current_bit = n & 1
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n >>= 1
        
        return True