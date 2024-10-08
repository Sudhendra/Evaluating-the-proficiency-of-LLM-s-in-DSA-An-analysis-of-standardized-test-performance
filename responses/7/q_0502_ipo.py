from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted([(capital[i], profits[i]) for i in range(n)], key=lambda x: x[0])

        available_projects = []
        current_capital = w

        for _ in range(k):
            while projects and projects[0][0] <= current_capital:
                project = projects.pop(0)
                capital_needed, profit = project
                available_projects.append(-profit)

            if not available_projects:
                break

            current_capital -= min(available_projects)
            available_projects.remove(min(available_projects))

        return current_capital

# Test the solution with examples from the problem
sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))  # Output: 4
print(sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))  # Output: 6
