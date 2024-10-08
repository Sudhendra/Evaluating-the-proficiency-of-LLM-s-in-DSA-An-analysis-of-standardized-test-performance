from itertools import combinations

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False

        n = len(nums)
        visited = [0] * n

        def dfs(k, start, current_sum):
            if k == 1:
                return True
            
            if current_sum == target:
                return dfs(k - 1, 0, 0)

            for i in range(start, n):
                if visited[i] or current_sum + nums[i] > target:
                    continue

                visited[i] = 1
                if dfs(k, i + 1, current_sum + nums[i]):
                    return True
                visited[i] = 0

            return False

        return dfs(k, 0, 0)