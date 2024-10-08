from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        
        side_length = perimeter // 4
        target = [side_length] * 4
        matchsticks.sort(reverse=True)
        
        def dfs(index, target):
            if index == n:
                return True
            for i in range(4):
                if target[i] >= matchsticks[index]:
                    target[i] -= matchsticks[index]
                    if dfs(index + 1, target):
                        return True
                    target[i] += matchsticks[index]
            return False
        
        return dfs(0, target)
