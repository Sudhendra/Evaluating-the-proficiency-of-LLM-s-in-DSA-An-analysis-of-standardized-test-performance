from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones_count = arr.count(1)
        
        if ones_count == 0:
            return [0, n - 1]

        if ones_count % 3 != 0:
            return [-1, -1]

        target_ones = ones_count // 3
        third_ones = 0
        end = n - 1

        while third_ones < target_ones:
            if arr[end] == 1:
                third_ones += 1
            end -= 1

        first_end = find_end(arr, 0, n - end - 2)
        if first_end == -1:
            return [-1, -1]

        second_end = find_end(arr, first_end + 1, n - end - 2)
        if second_end == -1:
            return [-1, -1]

        return [first_end, second_end + 1]

def find_end(arr, start, zeros_count):
    i = start
    ones_count = 0
    while i < len(arr) and zeros_count > 0:
        if arr[i] == 1:
            ones_count += 1
        else:
            zeros_count -= 1
        i += 1

    j = i
    while j < len(arr) and arr[j] == 0:
        j += 1

    if j <= len(arr) - 1 or ones_count == 0:
        return -1

    return i - 1
