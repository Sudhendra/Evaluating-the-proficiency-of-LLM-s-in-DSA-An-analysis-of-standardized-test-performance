class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        curr_max = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                curr_max = max(curr_max, jobs[j][1])
                j += 1
            max_profit += curr_max
        
        return max_profit