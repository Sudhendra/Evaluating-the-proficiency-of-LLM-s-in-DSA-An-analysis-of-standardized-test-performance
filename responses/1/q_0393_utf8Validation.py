class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(num: int) -> int:
            if num < 128:
                return 1
            elif num >> 5 == 6:
                return 2
            elif num >> 4 == 14:
                return 3
            elif num >> 3 == 30:
                return 4
            else:
                return 0
        
        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            if num_bytes == 0:
                return False
            
            for j in range(1, num_bytes):
                if i + j >= len(data) or data[i + j] >> 6 != 2:
                    return False
            
            i += num_bytes
        
        return True