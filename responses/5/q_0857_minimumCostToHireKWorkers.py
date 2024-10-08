from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(
            self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        result = float('inf')
        qualityHeap = []
        totalQuality = 0

        for workerRatio, workerQuality in workers:
            heapq.heappush(qualityHeap, -workerQuality)  # use negative quality for max heap
            totalQuality += workerQuality

            if len(qualityHeap) > k:
                totalQuality += heapq.heappop(qualityHeap)  # remove the max quality worker
            if len(qualityHeap) == k:
                result = min(result, totalQuality * workerRatio)

        return result
