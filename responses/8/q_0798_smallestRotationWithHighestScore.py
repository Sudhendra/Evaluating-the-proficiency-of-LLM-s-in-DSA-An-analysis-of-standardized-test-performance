from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        bad = [0] * n
        
        for i in range(n):
            left, right = (i - nums[i] + 1) % n, (i + 1) % n
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1
        
        res = cur = 0
        best = -n
        
        for i in range(n):
            cur += bad[i]
            if cur > best:
                best = cur
                res = i
        
        return res
