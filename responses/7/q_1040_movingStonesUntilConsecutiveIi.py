from typing import List

class Solution:

    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
        i, min_moves = 0, n
        j = 0
        for i in range(n):
            while stones[i] - stones[j] >= n:
                j += 1
            if i - j + 1 == n - 1 and stones[i] - stones[j] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - (i - j + 1))
        return [min_moves, max_moves]

