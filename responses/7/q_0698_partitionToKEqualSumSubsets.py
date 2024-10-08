from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        nums.sort(reverse=True)

        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        if nums[0] > target_sum:
            return False

        def backtrack(groups, index):
            if index == len(nums):
                return len(set(groups)) == 1

            for i in range(k):
                if groups[i] + nums[index] <= target_sum:
                    groups[i] += nums[index]
                    if backtrack(groups, index + 1):
                        return True
                    groups[i] -= nums[index]

                if groups[i] == 0:
                    break

            return False

        return backtrack([0] * k, 0)
