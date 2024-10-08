from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        i = 1

        while i < n - 1:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                max_length = max(max_length, right - left + 1)
                i = right
            else:
                i += 1
        
        return max_length
