from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones_count = arr.count(1)
        
        if ones_count == 0:
            return [0, 2]
        
        if ones_count % 3 != 0:
            return [-1, -1]
        
        target_ones = ones_count // 3
        first_end, second_end = -1, -1
        count, index = 0, len(arr) - 1
        
        while index >= 0:
            if arr[index] == 1:
                count += 1
                if count == target_ones:
                    if first_end == -1:
                        first_end = index
                        count = 0
                    elif second_end == -1:
                        second_end = index
                        break
            index -= 1
        
        cnt_zeros_after_first_end = len(arr) - first_end - 1
        cnt_zeros_after_second_end = len(arr) - second_end - 1
        
        if cnt_zeros_after_first_end < cnt_zeros_after_second_end or cnt_zeros_after_first_end < target_ones or cnt_zeros_after_second_end < target_ones:
            return [-1, -1]
        
        first_start = self.find_start(arr, 0, first_end)
        second_start = self.find_start(arr, first_start, second_end)
        
        while second_end < len(arr) and arr[first_start] == arr[second_start] == arr[second_end]:
            first_start += 1
            second_start += 1
            second_end += 1
        
        return [first_start - 1, second_start]

    def find_start(self, arr, start, end):
        while start < len(arr) and arr[start] == 0:
            start += 1

        return start
