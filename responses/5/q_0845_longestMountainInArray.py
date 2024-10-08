from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        i = 1

        while i < n - 1:
            is_peak = arr[i-1] < arr[i] > arr[i+1]
            if not is_peak:
                i += 1
                continue

            left = i - 2
            while left >= 0 and arr[left] < arr[left+1]:
                left -= 1

            right = i + 2
            while right < n and arr[right] < arr[right-1]:
                right += 1

            current_length = right - left - 1
            max_length = max(max_length, current_length)

            i = right

        return max_length
