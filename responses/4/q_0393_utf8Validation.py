from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(num: int) -> int:
            if num & 0b10000000 == 0:
                return 1
            elif num & 0b11100000 == 0b11000000:
                return 2
            elif num & 0b11110000 == 0b11100000:
                return 3
            elif num & 0b11111000 == 0b11110000:
                return 4
            else:
                return -1

        def is_valid_utf8(data: List[int], start: int) -> bool:
            num_bytes = get_num_bytes(data[start])
            if num_bytes == -1:
                return False

            for i in range(1, num_bytes):
                if start + i >= len(data):
                    return False
                if not (data[start + i] & 0b11000000 == 0b10000000):
                    return False

            return True

        i = 0
        while i < len(data):
            if not is_valid_utf8(data, i):
                return False
            i += get_num_bytes(data[i])

        return True
