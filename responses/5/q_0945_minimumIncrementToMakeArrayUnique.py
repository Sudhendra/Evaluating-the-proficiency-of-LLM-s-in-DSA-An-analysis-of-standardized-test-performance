from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = [0] * (2 * 10**5 + 1)
        max_val = float('-inf')
        
        for num in nums:
            count[num] += 1
            max_val = max(max_val, num)
        
        moves = 0
        taken = 0
        
        for i in range(1, max_val + 1):
            if count[i] >= 2:
                taken += count[i] - 1
                moves -= i * (count[i] - 1)
            elif taken > 0 and count[i] == 0:
                taken -= 1
                moves += i
        
        for i in range(max_val + 1, len(count)):
            if taken > 0 and count[i] == 0:
                taken -= 1
                moves += i
        
        return moves
