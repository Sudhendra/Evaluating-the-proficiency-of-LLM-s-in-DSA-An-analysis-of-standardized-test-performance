from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = sum(arr)
        if n % 3 != 0:
            return [-1, -1]
        
        if n == 0:
            return [0, len(arr) - 1]
        
        third_part_end = len(arr) - 1
        third_part_cnt_ones = n // 3
        
        cnt_ones = 0
        first_part_end, second_part_end = -1, -1
        
        for i in range(len(arr)):
            if arr[i] == 1:
                cnt_ones += 1
                
                if cnt_ones == 1:
                    first_part_end = i
                
                if cnt_ones == third_part_cnt_ones + 1:
                    second_part_end = i
                
                if cnt_ones == 2 * third_part_cnt_ones:
                    shift = 0
                    while i < third_part_end:
                        if arr[first_part_end + shift] != arr[i] or arr[second_part_end + shift] != arr[i + third_part_cnt_ones]:
                            return [-1, -1]
                        shift += 1
                        i += 1
                    return [first_part_end + shift, second_part_end + shift]
        
        return [-1, -1]
