from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(reverse=True)

        available_projects = []
        idx = 0

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(available_projects, -projects[idx][1])
                idx += 1

            if available_projects:
                w -= heapq.heappop(available_projects)
            else:
                break

        return w

# Note: Multiple solutions are not required for this problem
