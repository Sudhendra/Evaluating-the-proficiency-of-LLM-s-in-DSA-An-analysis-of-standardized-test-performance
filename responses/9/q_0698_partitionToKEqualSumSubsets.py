from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False

        nums.sort(reverse=True)
        groups = [0] * k

        def dfs(index):
            if index == len(nums):
                return True
            num = nums[index]

            for i in range(k):
                if groups[i] + num <= target:
                    groups[i] += num
                    if dfs(index + 1):
                        return True
                    groups[i] -= num
                if groups[i] == 0:
                    break
            return False

        return dfs(0)
