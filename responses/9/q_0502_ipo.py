from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available_projects = []
        idx = 0

        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                available_projects.append(-projects[idx][1])
                idx += 1
            if not available_projects:
                break
            w -= heapq.heappop(available_projects)

        return w
