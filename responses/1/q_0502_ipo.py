from typing import List
import heapq

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        available_projects = []
        n = len(projects)
        i = 0
        
        for _ in range(k):
            while i < n and projects[i][1] <= w:
                heapq.heappush(available_projects, -projects[i][0])
                i += 1
            if not available_projects:
                break
            w -= heapq.heappop(available_projects)

        return w
