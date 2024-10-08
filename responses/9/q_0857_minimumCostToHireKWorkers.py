from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        heap = []
        sumq = 0
        ans = float('inf')

        for r, q in workers:
            heapq.heappush(heap, -q)
            sumq += q

            if len(heap) > k:
                sumq += heapq.heappop(heap)

            if len(heap) == k:
                ans = min(ans, r * sumq)

        return ans
