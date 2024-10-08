class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = 1
        while mask < n:
            mask = (mask << 1) | 1

        return n ^ mask
