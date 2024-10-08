from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        
        last_stone = stones[-1]
        
        dp = {}  # Dictionary to keep track of stones and the jump sizes used to reach them
        
        for stone in stones:
            dp[stone] = set()  # Initialize an empty set for each stone
        
        dp[0].add(0)  # Initial stone with jump size 0
        
        for stone in stones:
            for jump in dp[stone]:  # Check possible jumps from current stone
                for new_jump in range(jump - 1, jump + 2):  # Next possible jump sizes
                    if new_jump > 0 and stone + new_jump in dp:  # Check if stone can be reached
                        dp[stone + new_jump].add(new_jump)  # Add new jump size to the destination stone's set
        
        return len(dp[last_stone]) > 0
