from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        for i in range(1, n-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                left = right = i
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1
                max_length = max(max_length, right - left + 1)
        
        return max_length
