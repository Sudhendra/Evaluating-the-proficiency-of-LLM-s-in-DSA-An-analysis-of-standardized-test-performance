from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones_count = arr.count(1)
        
        if ones_count == 0:
            return [0, len(arr) - 1]
        if ones_count % 3 != 0:
            return [-1, -1]
        
        target_ones = ones_count // 3
        if target_ones == 0:
            return [0, len(arr) - 1]
        
        # Finding the ending zeros for each part
        end_zeros_count = 0
        target_zeros = 0
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                end_zeros_count += 1
            if arr[i] == 1:
                if target_zeros < end_zeros_count:
                    target_zeros = end_zeros_count
                if end_zeros_count < target_zeros:
                    res.append(len(arr) - i - 1)
                    end_zeros_count = 0
        
        res.reverse()
        
        # Checking if the parts are equal
        while res:
            part_len = len(arr) - res.pop()
            for i in range(part_len):
                if arr[i] != arr[i + part_len] or arr[i] != arr[i + 2 * part_len]:
                    return [-1, -1]
        
        return [res[0], res[1] + 1]
