from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        
        side_len = total_len // 4
        sides = [0] * 4
        
        matchsticks.sort(reverse=True)
        
        def dfs(index):
            if index == len(matchsticks):
                return all(side == side_len for side in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_len:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
            return False
        
        return dfs(0)
