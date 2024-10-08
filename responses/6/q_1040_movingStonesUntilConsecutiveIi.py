from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_moves = max(stones[-1]-stones[1]-(n-2), stones[-2]-stones[0]-(n-2)) - (n-2)
        min_moves = n
        i, j = 0, 0
        for i in range(n):
            while j+1 < n and stones[j+1] - stones[i] + 1 <= n:
                j += 1
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            min_moves = min(min_moves, cost)
        return [min_moves, max_moves]
