class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Step 1: Compute the sums of every subarray of size k
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        sum_1, sum_2, sum_3 = 0, 0, 0
        dp = [[None, None] for _ in range(n+1)]

        # Step 2: Calculate the maximum sum of one subarray on the left side
        for i in range(k, n+1):
            sub_sum = sums[i] - sums[i-k]
            if sub_sum > sum_1:
                sum_1 = sub_sum
            dp[i][0] = sum_1

        # Step 3: Calculate the maximum sum of two non-overlapping subarrays
        for i in range(2 * k, n+1):
            sub_sum = sums[i] - sums[i-k] + dp[i-k][0]
            if sub_sum > sum_2:
                sum_2 = sub_sum
            dp[i][1] = sum_2

        # Step 4: Calculate the maximum sum of three non-overlapping subarrays
        res = []
        for i in range(3 * k, n+1):
            sub_sum = sums[i] - sums[i-k] + dp[i-k][1]
            if sub_sum > sum_3:
                sum_3 = sub_sum
                res = [i-3*k, i-2*k, i-k]

        return res
