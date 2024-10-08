from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted([(capital[i], profits[i]) for i in range(n)], reverse=True)
        
        available_projects = []
        idx = 0
        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                available_projects.append(projects[idx][1])
                idx += 1
            if not available_projects:
                break
            w += max(available_projects)
            available_projects.remove(max(available_projects))
        
        return w
