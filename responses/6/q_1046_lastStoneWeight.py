class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        
        return 0 if not stones else -stones[0]
