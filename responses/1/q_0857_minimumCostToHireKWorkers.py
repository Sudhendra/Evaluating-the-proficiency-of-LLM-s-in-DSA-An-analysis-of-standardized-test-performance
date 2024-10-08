from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        heap = []
        total_quality = 0
        ans = float('inf')

        for ratio, q in workers:
            total_quality += q
            heap.append(-q)
            if len(heap) > k:
                total_quality += heap.pop()
            if len(heap) == k:
                ans = min(ans, ratio * total_quality)

        return ans