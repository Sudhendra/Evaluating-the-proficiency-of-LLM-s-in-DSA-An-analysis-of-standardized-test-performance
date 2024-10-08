from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(byte):
            if byte >> 7 == 0b0:
                return 1
            elif byte >> 5 == 0b110:
                return 2
            elif byte >> 4 == 0b1110:
                return 3
            elif byte >> 3 == 0b11110:
                return 4
            else:
                return 0
        
        def check_continuation(start, end):
            for i in range(start+1, end+1):
                if data[i] >> 6 != 0b10:
                    return False
            return True
        
        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            if num_bytes == 0:
                return False
            if not check_continuation(i, i + num_bytes - 1):
                return False
            i += num_bytes
        
        return True
