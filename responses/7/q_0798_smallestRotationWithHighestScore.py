from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        bad = [0] * n
        
        for i in range(n):
            left = (i - nums[i] + 1) % n
            right = (i + 1) % n
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1
        
        curr = 0
        best = 0
        result = 0
        for i in range(n):
            curr += bad[i]
            if curr > best:
                best = curr
                result = i + 1
        
        return result
