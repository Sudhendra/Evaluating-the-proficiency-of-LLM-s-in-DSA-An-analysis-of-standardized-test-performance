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

        start, mid, end = None, None, None
        count = 0

        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                if count == 1:
                    start = i
                elif count == target_ones + 1:
                    mid = i
                elif count == 2 * target_ones + 1:
                    end = i

        while end < len(arr) and arr[start] == arr[mid] == arr[end]:
            start += 1
            mid += 1
            end += 1

        if end == len(arr):
            return [start - 1, mid]
        else:
            return [-1, -1]
