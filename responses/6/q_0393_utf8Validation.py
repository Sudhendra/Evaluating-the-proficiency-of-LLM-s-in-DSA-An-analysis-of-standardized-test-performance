from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bytes_to_follow = 0
        for num in data:
            if bytes_to_follow == 0:
                if (num >> 5) == 0b110:
                    bytes_to_follow = 1
                elif (num >> 4) == 0b1110:
                    bytes_to_follow = 2
                elif (num >> 3) == 0b11110:
                    bytes_to_follow = 3
                elif (num >> 7):
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                bytes_to_follow -= 1
        return bytes_to_follow == 0
