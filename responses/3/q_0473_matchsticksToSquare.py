from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        target_side_length = total_length // 4
        matchsticks.sort(reverse=True)
        
        def dfs(index, sides):
            if index == len(matchsticks):
                return all(side == target_side_length for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= target_side_length:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1, sides):
                        return True
                    sides[i] -= matchsticks[index]
            return False
        
        return dfs(0, [0, 0, 0, 0])
