from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(distances)
        return [heapq.heappop(distances)[1] for _ in range(k)]