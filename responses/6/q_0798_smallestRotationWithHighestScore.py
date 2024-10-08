from collections import Counter
from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        bad = [0] * n
        for i in range(n):
            l = (i - nums[i] + 1) % n
            r = (i + 1) % n
            bad[l] -= 1
            bad[r] += 1
            if l > r:
                bad[0] -= 1
        score = [0] * n
        score[0] = sum(bad)
        for i in range(1, n):
            score[i] = score[i - 1] + bad[i - 1]
        return score.index(max(score))
