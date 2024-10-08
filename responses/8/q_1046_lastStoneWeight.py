from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones.pop(), stones.pop()
            if x != y:
                stones.append(abs(x - y))
        return stones[0] if stones else 0
