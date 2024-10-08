from typing import List

class Solution:
    
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        n = len(difficulty)
        max_profit = 0

        jobs = list(zip(difficulty, profit)) # Combine difficulty and profit into tuples
        jobs.sort() # Sort jobs by difficulty

        worker.sort() # Sort workers' abilities

        current_max_profit = 0
        j = 0 # Pointer for jobs
        for ability in worker:
            while j < n and jobs[j][0] <= ability:
                current_max_profit = max(current_max_profit, jobs[j][1])
                j += 1
            max_profit += current_max_profit

        return max_profit

# Example usage
sol = Solution()
print(sol.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])) # Output: 100
print(sol.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25])) # Output: 0
