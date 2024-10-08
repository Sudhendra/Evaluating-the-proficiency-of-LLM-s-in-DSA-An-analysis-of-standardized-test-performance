from typing import List

class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y - x))
        
        return 0 if not stones else -stones[0]
