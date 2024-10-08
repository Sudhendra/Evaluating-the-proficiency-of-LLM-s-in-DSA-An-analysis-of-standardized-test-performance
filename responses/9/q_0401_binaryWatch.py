from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_set_bits(num: int) -> int:
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        def format_time(hour: int, minute: int) -> str:
            return str(hour) + ":" + str(minute).zfill(2)

        results = []

        for h in range(12):
            for m in range(60):
                if count_set_bits(h) + count_set_bits(m) == turnedOn:
                    results.append(format_time(h, m))

        return results
