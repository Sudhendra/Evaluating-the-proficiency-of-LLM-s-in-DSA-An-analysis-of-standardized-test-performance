from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones_count = arr.count(1)

        if ones_count == 0:
            return [0, len(arr) - 1]

        if ones_count % 3 != 0:
            return [-1, -1]

        target_ones_count = ones_count // 3

        indices = [i for i, num in enumerate(arr) if num == 1]

        first_start = indices[0]
        second_start = indices[target_ones_count]
        third_start = indices[2 * target_ones_count]

        while third_start < len(arr) and arr[first_start] == arr[second_start] == arr[third_start]:
            first_start += 1
            second_start += 1
            third_start += 1

        if third_start == len(arr):
            return [first_start - 1, second_start]

        return [-1, -1]
