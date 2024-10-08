from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(num: int) -> int:
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count

        result = []
        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result
