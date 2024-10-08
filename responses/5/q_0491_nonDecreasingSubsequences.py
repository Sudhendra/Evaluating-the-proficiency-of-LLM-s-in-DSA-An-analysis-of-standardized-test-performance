class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, nums, res):
            if len(path) > 1:
                res.append(path[:])
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i+1, path, nums, res)
                    path.pop()
        
        res = []
        backtrack(0, [], nums, res)
        return res