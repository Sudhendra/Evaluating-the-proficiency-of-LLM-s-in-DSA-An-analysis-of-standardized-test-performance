from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False
        
        def backtrack(groups):
            if not nums:
                return True
            num = nums.pop()
            for i, group in enumerate(groups):
                if group + num <= target:
                    groups[i] += num
                    if backtrack(groups):
                        return True
                    groups[i] -= num
                if not group:
                    break
                if group + num == target:  # optimization to avoid permutations
                    break
            nums.append(num)
            return False
        
        nums.sort()
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return backtrack([0] * k)
