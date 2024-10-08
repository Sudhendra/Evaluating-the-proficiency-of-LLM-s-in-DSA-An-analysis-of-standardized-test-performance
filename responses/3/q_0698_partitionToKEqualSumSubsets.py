from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder != 0 or max(nums) > target:
            return False
        
        nums.sort(reverse=True)
        groups = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return len(set(groups)) == 1
            
            for i in range(k):
                groups[i] += nums[index]
                if groups[i] <= target and backtrack(index + 1):
                    return True
                groups[i] -= nums[index]
                if groups[i] == 0:
                    break
            return False
        
        return backtrack(0)