class Solution:
    """Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values."""

    def hasAlternatingBits(self, n: int) -> bool:
        previous_bit = n & 1
        n >>= 1
        while n:
            current_bit = n & 1
            if current_bit == previous_bit:
                return False
            previous_bit = current_bit
            n >>= 1
        return True
