class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # Get the leftmost set bit position
        leftmost_set_bit = 0
        temp = n
        while temp > 0:
            leftmost_set_bit += 1
            temp = temp >> 1
        # XOR the number with a number that has 1s at positions less than leftmost_set_bit
        return n ^ ((1 << leftmost_set_bit) - 1)
