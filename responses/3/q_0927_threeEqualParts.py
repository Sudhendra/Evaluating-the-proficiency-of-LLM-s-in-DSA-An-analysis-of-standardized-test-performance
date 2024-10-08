from typing import List

class Solution:    
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones_count = sum(arr)
        if ones_count % 3 != 0:
            return [-1, -1]
        
        if ones_count == 0:
            return [0, len(arr) - 1]
        
        ones_per_part = ones_count // 3
        third_part_start = len(arr)
        
        count = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1:
                count += 1
                if count == ones_per_part:
                    third_part_start = i
                    break
        
        i = self.find_end_of_first_part(arr, ones_per_part)
        j = self.find_end_of_second_part(arr, ones_per_part, third_part_start)
        
        while j < len(arr) and arr[i] == arr[j] == arr[third_part_start]:
            i += 1
            j += 1
            third_part_start += 1
        
        if j == len(arr):
            return [i-1, j]
        return [-1, -1]
    
    def find_end_of_first_part(self, arr, ones_per_part):
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                if count == ones_per_part:
                    return i
        return -1
    
    def find_end_of_second_part(self, arr, ones_per_part, third_part_start):
        count = 0
        for i in range(third_part_start, len(arr)):
            if arr[i] == 1:
                count += 1
                if count == ones_per_part:
                    return i
        return -1
