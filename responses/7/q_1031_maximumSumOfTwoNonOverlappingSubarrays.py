```python
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        result = 0
        for i in range(len(nums) - firstLen + 1):
            for j in range(i + firstLen, len(nums) - secondLen + 1):
                result = max(result, prefix_sum[i + firstLen] - prefix_sum[i] + max(prefix_sum[j + secondLen] - prefix_sum[j], prefix_sum[j + secondLen + firstLen] - prefix_sum[j + secondLen]))
        
        return result
```
This code implements the `maxSumTwoNoOverlap` method that calculates the maximum sum of elements in two non-overlapping subarrays with given lengths in the input numeric array.