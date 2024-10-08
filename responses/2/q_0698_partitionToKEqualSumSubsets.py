from typing import List

class Solution:
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k
        if sum(nums) % k != 0 or max(nums) > target:
            return False

        def backtrack(groups, idx):
            if idx == len(nums):
                return len(set(groups)) == 1

            num = nums[idx]
            for i in range(k):
                if groups[i] + num <= target:
                    groups[i] += num
                    if backtrack(groups, idx + 1):
                        return True
                    groups[i] -= num

                if groups[i] == 0:
                    break

            return False

        nums.sort(reverse=True)
        return backtrack([0] * k, 0)
