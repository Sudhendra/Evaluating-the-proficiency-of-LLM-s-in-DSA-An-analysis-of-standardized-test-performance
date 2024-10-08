class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(val):
            if val & 0b10000000 == 0:
                return 1
            elif val & 0b11100000 == 0b11000000:
                return 2
            elif val & 0b11110000 == 0b11100000:
                return 3
            elif val & 0b11111000 == 0b11110000:
                return 4
            else:
                return -1

        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            if num_bytes == -1:
                return False
            i += 1
            while num_bytes > 1:
                if i >= len(data) or data[i] & 0b11000000 != 0b10000000:
                    return False
                i += 1
                num_bytes -= 1
        return True