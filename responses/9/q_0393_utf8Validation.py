from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(byte):
            if byte & 0b10000000 == 0:
                return 1
            num_bytes = 0
            mask = 0b10000000
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            return num_bytes

        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            if num_bytes == 1 or num_bytes > 4:
                return False
            for j in range(1, num_bytes):
                if i + j >= len(data) or (data[i + j] & 0b11000000) != 0b10000000:
                    return False
            i += num_bytes
        return True

# Sample test cases
solution = Solution()
print(solution.validUtf8([197,130,1]))  # Output: True
print(solution.validUtf8([235,140,4]))  # Output: False
