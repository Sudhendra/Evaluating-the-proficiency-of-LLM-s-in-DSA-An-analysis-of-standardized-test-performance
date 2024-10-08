from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        def get_time_string(hours, minutes):
            return f"{hours}:{minutes:02d}"

        valid_times = []
        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    valid_times.append(get_time_string(hour, minute))

        return valid_times
