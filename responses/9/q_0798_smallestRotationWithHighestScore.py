from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        bad = [0] * n

        for i, num in enumerate(nums):
            left = (i - num) % n
            right = (i + 1) % n

            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        cur_bad = 0
        best_k = 0
        max_score = 0
        cur_score = 0

        for k, b in enumerate(bad):
            cur_bad += b
            if cur_bad > max_score:
                max_score = cur_bad
                best_k = k

        return best_k
