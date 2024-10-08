from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))
        best_quality = []
        total_quality = 0
        result = float('inf')

        for ratio, q in workers:
            total_quality += q
            heapq.heappush(best_quality, -q)
            if len(best_quality) > k:
                total_quality += heapq.heappop(best_quality)
            if len(best_quality) == k:
                result = min(result, total_quality * ratio)

        return result
