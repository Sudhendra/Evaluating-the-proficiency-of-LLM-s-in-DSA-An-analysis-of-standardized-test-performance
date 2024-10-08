class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining_bytes = 0
        
        for num in data:
            byte = num & 255  # Get only the last 8 bits
            if remaining_bytes == 0:
                if byte >> 7 == 0b0:  # 1-byte character
                    continue
                elif byte >> 5 == 0b110:  # 2-byte character
                    remaining_bytes = 1
                elif byte >> 4 == 0b1110:  # 3-byte character
                    remaining_bytes = 2
                elif byte >> 3 == 0b11110:  # 4-byte character
                    remaining_bytes = 3
                else:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                remaining_bytes -= 1
        
        return remaining_bytes == 0
