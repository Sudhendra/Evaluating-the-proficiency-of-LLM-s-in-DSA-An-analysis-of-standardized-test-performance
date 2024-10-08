from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])
        
        def median(window):
            n = len(window)
            if n % 2 == 0:
                return (window[n // 2] + window[n // 2 - 1]) / 2
            else:
                return window[n // 2]

        result.append(median(window))

        for i in range(k, len(nums)):
            window.discard(nums[i - k])
            window.add(nums[i])
            result.append(median(window))

        return result