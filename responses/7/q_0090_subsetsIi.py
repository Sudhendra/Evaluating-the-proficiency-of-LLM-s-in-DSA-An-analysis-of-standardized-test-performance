from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.generate_subsets(nums, 0, [], subsets)
        return subsets
        
    def generate_subsets(self, nums, index, path, subsets):
        subsets.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.generate_subsets(nums, i+1, path + [nums[i]], subsets)
