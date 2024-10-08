from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available_projects = []
        idx = 0

        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(available_projects, -projects[idx][1])
                idx += 1
            if not available_projects:
                break
            w -= heapq.heappop(available_projects)

        return w

# Unit tests
solution = Solution()
assert solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
assert solution.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
