from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        target_side_length = total_length // 4
        matchsticks.sort(reverse=True)
        used = [False] * len(matchsticks)
        
        def dfs(index, side_count, current_length):
            if side_count == 4:
                return True
                
            if current_length == target_side_length:
                return dfs(0, side_count + 1, 0)
            
            for i in range(index, len(matchsticks)):
                if not used[i] and current_length + matchsticks[i] <= target_side_length:
                    used[i] = True
                    if dfs(i + 1, side_count, current_length + matchsticks[i]):
                        return True
                    used[i] = False
            return False
        
        return dfs(0, 0, 0)
