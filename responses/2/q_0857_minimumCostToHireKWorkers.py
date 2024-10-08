from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        heap = []
        sumq = 0
        ans = float('inf')

        for ratio, q in workers:
            sumq += q
            heapq.heappush(heap, -q)
            
            if len(heap) > k:
                sumq += heapq.heappop(heap)  # remove the maximum quality
            
            if len(heap) == k:
                ans = min(ans, ratio * sumq)
        
        return float(ans)
