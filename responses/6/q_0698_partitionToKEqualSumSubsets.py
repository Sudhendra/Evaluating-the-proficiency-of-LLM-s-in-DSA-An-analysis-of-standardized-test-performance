from itertools import product

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem != 0 or max(nums) > target:
            return False

        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        total = [0] * (1 << n)

        for mask in range(1 << n):
            if not dp[mask]:
                continue
            for i in range(n):
                if not (mask & (1 << i)) and dp[mask | (1 << i)] == False:
                    next_mask = mask | (1 << i)
                    if total[mask] % target + nums[i] <= target:
                        dp[next_mask] = True
                        total[next_mask] = total[mask] + nums[i]
                    else:
                        break

        return dp[-1]
