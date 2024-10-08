from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False
        
        nums.sort(reverse=True)
        groups = [0] * k
        
        def backtrack(idx):
            if idx == len(nums):
                return len(set(groups)) == 1
            
            num = nums[idx]
            for i in range(k):
                if groups[i] + num <= target:
                    groups[i] += num
                    if backtrack(idx + 1):
                        return True
                    groups[i] -= num
                if groups[i] == 0:  # optimization to avoid permutations of empty groups
                    break
            return False
        
        return backtrack(0)
