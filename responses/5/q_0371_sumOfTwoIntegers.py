from typing import Tuple

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # Mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative
        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)