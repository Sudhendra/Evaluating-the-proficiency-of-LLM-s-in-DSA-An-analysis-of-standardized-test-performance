from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.generate_subsets([], 0, nums, subsets)
        return subsets
    
    def generate_subsets(self, current, index, nums, subsets):
        subsets.append(list(current))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.generate_subsets(current, i+1, nums, subsets)
            current.pop()
