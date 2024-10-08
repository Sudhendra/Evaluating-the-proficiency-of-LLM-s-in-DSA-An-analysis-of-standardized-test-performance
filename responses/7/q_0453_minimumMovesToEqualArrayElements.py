from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        total_moves = 0
        
        for num in nums:
            total_moves += num - min_num
        
        return total_moves
