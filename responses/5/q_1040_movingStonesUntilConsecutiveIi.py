from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        low_moves = float('inf')
        low = 0
        high = 0

        for i in range(n):
            while stones[i] - stones[low] >= n:
                low += 1
            low_moves = min(low_moves, n - (i - low + 1))

            if i - low + 1 == n - 1 and stones[i] - stones[low] == n - 2:
                low_moves = min(low_moves, 2)

        high = max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2)

        return [low_moves, high]
