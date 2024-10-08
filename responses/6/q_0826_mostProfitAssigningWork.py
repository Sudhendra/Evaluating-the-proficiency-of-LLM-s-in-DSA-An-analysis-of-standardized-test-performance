from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))  # Combine difficulty and profit, then sort by difficulty
        worker.sort()  # Sort workers by ability

        max_profit = 0
        i = 0
        best_profit = 0

        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            max_profit += best_profit

        return max_profit
