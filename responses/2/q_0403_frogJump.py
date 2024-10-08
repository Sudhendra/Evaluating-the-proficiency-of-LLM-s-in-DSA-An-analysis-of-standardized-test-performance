from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last_stone = stones[-1]
        stones_set = set(stones)
        
        @lru_cache(None)
        def dfs(position, jump):
            if position == last_stone:
                return True
            
            for next_jump in [jump-1, jump, jump+1]:
                if next_jump <= 0:
                    continue
                next_position = position + next_jump
                if next_position in stones_set and dfs(next_position, next_jump):
                    return True
            
            return False
        
        return dfs(0, 0)