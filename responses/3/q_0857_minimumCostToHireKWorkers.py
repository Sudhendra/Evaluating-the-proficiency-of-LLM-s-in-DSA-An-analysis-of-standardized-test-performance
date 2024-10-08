from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        total_cost = float('inf')
        quality_sum = 0
        heap = []
        
        for ratio, q in workers:
            quality_sum += q
            heapq.heappush(heap, -q)
            
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
                
            if len(heap) == k:
                total_cost = min(total_cost, quality_sum * ratio)
        
        return total_cost
