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

        k = bestK = 0
        bestScore = curScore = 0

        for i in range(n):
            curScore += bad[i]
            if curScore > bestScore:
                bestScore = curScore
                bestK = k
            k += 1

        return bestK
