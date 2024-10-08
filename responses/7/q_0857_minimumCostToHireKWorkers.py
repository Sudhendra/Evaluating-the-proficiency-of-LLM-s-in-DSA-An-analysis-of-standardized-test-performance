from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratios = []
        for i in range(n):
            ratios.append((wage[i] / quality[i], quality[i]))
        ratios.sort()

        min_cost = float('inf')
        quality_sum = 0
        heap = []

        for ratio, q in ratios:
            quality_sum += q
            heapq.heappush(heap, -q)
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            if len(heap) == k:
                min_cost = min(min_cost, ratio * quality_sum)

        return min_cost

# Example usage
solution = Solution()
print(solution.mincostToHireWorkers([10,20,5], [70,50,30], 2))  # Output: 105.0
print(solution.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))  # Output: 30.666666666666668
