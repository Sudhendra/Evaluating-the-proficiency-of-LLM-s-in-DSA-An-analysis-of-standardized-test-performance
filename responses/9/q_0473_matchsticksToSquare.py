from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        target_side = total_length // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return all(side == target_side for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[index] <= target_side:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
            return False

        return dfs(0)
