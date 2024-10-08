from collections import Counter

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
        
        max_score = 0
        best_k = 0
        cur_score = 0
        
        for i in range(n):
            cur_score += bad[i]
            if cur_score > max_score:
                max_score = cur_score
                best_k = i
        
        return best_k
