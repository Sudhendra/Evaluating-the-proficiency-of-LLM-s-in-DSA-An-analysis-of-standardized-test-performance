from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        max_profit = 0
        
        jobs = sorted(zip(difficulty, profit))  # Sort jobs based on difficulty
        
        worker.sort()  # Sort workers based on their ability
        
        j = 0
        best = 0
        
        for ability in worker:
            while j < n and jobs[j][0] <= ability:  # Find the best profit job worker can complete
                best = max(best, jobs[j][1])
                j += 1
            
            max_profit += best
        
        return max_profit

# Example usage:
# difficulty = [2,4,6,8,10]
# profit = [10,20,30,40,50]
# worker = [4,5,6,7]
# print(Solution().maxProfitAssignment(difficulty, profit, worker))  # Output: 100
