from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList(nums[:k])
        
        for i in range(k, len(nums)+1):
            if k % 2 == 0:
                median = (window[k//2 - 1] + window[k//2]) / 2
            else:
                median = window[k//2]

            result.append(float(median))

            if i < len(nums):
                window.discard(nums[i-k])
                window.add(nums[i])

        return result
