from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        max_profit = 0

        jobs = sorted(zip(difficulty, profit))       # Sort jobs by difficulty

        worker.sort()                               # Sort workers by abilities
        worker_idx, best_profit = 0, 0

        for ability in worker:
            while worker_idx < n and jobs[worker_idx][0] <= ability:
                best_profit = max(best_profit, jobs[worker_idx][1])
                worker_idx += 1
            max_profit += best_profit
        
        return max_profit
