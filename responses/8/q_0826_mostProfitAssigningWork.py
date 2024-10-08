from typing import List

class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        cur_max_profit = max_profit = i = 0
        
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                cur_max_profit = max(cur_max_profit, jobs[i][1])
                i += 1
            max_profit += cur_max_profit
        
        return max_profit
