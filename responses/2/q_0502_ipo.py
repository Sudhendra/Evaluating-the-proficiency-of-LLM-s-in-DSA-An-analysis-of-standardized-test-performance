from typing import List

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        projects = sorted([(capital[i], profits[i]) for i in range(n)], reverse=True)
        available_projects = []
        idx = 0

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                project_capital, project_profit = projects[idx]
                available_projects.append((-project_profit, project_capital))
                idx += 1

            if not available_projects:
                break
            
            available_projects.sort()
            profit, needed_capital = available_projects.pop()
            w += -profit
        
        return w