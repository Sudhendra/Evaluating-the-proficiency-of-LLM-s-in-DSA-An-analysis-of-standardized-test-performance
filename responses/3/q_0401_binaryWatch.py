from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        result = []
        for h in range(12):
            for m in range(60):
                if count_bits(h) + count_bits(m) == turnedOn:
                    result.append(f"{h}:{m:02}")
        return result
