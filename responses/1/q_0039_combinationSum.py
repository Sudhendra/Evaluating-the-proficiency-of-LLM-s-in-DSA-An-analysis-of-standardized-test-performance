class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, path, current_sum):
            if current_sum == target:
                output.append(path[:])
                
            for i in range(start, len(candidates)):
                if current_sum + candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(i, path, current_sum + candidates[i])
                    path.pop()
        
        output = []
        backtrack(0, [], 0)
        return output