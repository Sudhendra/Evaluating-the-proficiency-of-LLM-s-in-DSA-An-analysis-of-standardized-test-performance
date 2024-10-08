from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False

        nums.sort(reverse=True)
        
        def backtrack(groups):
            if not nums:
                return True
            num = nums.pop(0)
            for i in range(k):
                if groups[i] + num <= target:
                    groups[i] += num
                    if backtrack(groups):
                        return True
                    groups[i] -= num
                if groups[i] == 0:
                    break
                if groups[i] + num == target:
                    break
            nums.insert(0, num)
            return False

        return backtrack([0] * k)
