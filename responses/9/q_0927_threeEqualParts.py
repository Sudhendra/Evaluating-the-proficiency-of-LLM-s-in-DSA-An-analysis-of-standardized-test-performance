from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        num_ones = sum(arr)
        
        if num_ones % 3 != 0:
            return [-1, -1]
        
        if num_ones == 0:
            return [0, len(arr) - 1]
        
        target_ones = num_ones // 3
        idx1, idx2, idx3 = -1, -1, -1
        count_ones = 0
        
        for i, num in enumerate(arr):
            if num == 1:
                count_ones += 1
                if count_ones == 1:
                    idx1 = i
                elif count_ones == target_ones + 1:
                    idx2 = i
                elif count_ones == 2 * target_ones + 1:
                    idx3 = i
        
        while idx3 < len(arr) and arr[idx1] == arr[idx2] == arr[idx3]:
            idx1 += 1
            idx2 += 1
            idx3 += 1
        
        if idx3 == len(arr):
            return [idx1 - 1, idx2]
        
        return [-1, -1]
