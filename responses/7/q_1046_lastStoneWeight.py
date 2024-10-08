from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest1 = stones.pop()
            heaviest2 = stones.pop()
            if heaviest1 != heaviest2:
                stones.append(heaviest1 - heaviest2)
        return stones[0] if stones else 0
