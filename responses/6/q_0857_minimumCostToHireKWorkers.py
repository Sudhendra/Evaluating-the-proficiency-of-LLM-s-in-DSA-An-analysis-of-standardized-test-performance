from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        heap = []
        sumq = 0
        ans = float('inf')

        for ratio, qual in workers:
            sumq += qual
            heap.append(-qual)
            heap.sort()

            if len(heap) > k:
                sumq += heap.pop()

            if len(heap) == k:
                ans = min(ans, sumq * ratio)

        return ans
