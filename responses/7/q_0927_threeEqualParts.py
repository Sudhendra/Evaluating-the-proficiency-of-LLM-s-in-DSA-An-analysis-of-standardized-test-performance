from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        # Count the number of ones in the array
        ones_count = sum(arr)
        
        # If the number of ones is not divisible by 3, return [-1, -1]
        if ones_count % 3 != 0:
            return [-1, -1]
        
        # If there are no ones in the array, return [0, n-1]
        if ones_count == 0:
            return [0, n - 1]
        
        # Calculate the target number of ones in each part
        target_ones = ones_count // 3
        
        # Find the indices where the first part and the second part ends
        first_end = find_end(arr, 0, target_ones)
        if first_end == -1:
            return [-1, -1]
        
        second_end = find_end(arr, first_end + 1, target_ones)
        if second_end == -1:
            return [-1, -1]
        
        # Find the common prefix length among all three parts
        prefix_length = find_prefix_length(arr, first_end, second_end)
        
        # Skip trailing zeros in all three parts
        first_start = skip_zeros(arr, 0)
        second_start = skip_zeros(arr, first_end + 1)
        third_start = skip_zeros(arr, second_end + 1)
        
        # Check if the parts are equal
        while third_start < n:
            if arr[first_start] != arr[second_start] or arr[second_start] != arr[third_start]:
                return [-1, -1]
            
            first_start += 1
            second_start += 1
            third_start += 1
        
        return [first_end, second_end + 1]

def find_end(arr, start, target_ones):
    ones_count = 0
    for i in range(start, len(arr)):
        ones_count += arr[i]
        if ones_count == target_ones:
            return i
    return -1

def find_prefix_length(arr, end1, end2):
    common_length = 0
    length1 = end1 - 0 + 1
    length2 = end2 - end1
    while common_length < length1 and common_length < length2:
        if arr[0 + common_length] != arr[end1 + 1 + common_length] or arr[end1 + 1 + common_length] != arr[end2 + 1 + common_length]:
            break
        common_length += 1
    return common_length

def skip_zeros(arr, start):
    while start < len(arr) and arr[start] == 0:
        start += 1
    return start
