from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n: int) -> int:
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        def get_time_str(hour: int, minute: int) -> str:
            return f"{hour}:{minute:02d}"

        times = []
        for h in range(12):
            for m in range(60):
                if count_bits(h) + count_bits(m) == turnedOn:
                    times.append(get_time_str(h, m))

        return times
