class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0] * (n - k + 1)
        for i in range(k):
            sums[0] += nums[i]
        for i in range(1, n - k + 1):
            sums[i] = sums[i - 1] + nums[i + k - 1] - nums[i - 1]

        left_max = [0] * (n - 3*k + 1)
        left_max_idx = 0
        for i in range(n - 3*k + 1):
            if sums[i] > sums[left_max_idx]:
                left_max_idx = i
            left_max[i] = left_max_idx

        right_max = [0] * (n - 3*k + 1)
        right_max_idx = n - k
        for i in range(n - 3*k, -1, -1):
            if sums[i + 2*k] >= sums[right_max_idx]:
                right_max_idx = i
            right_max[i] = right_max_idx

        max_sum = float('-inf')
        res = []
        for i in range(k, n - 2*k + 1):
            j = left_max[i - k]
            l = right_max[i + k]
            total_sum = sums[j] + sums[i] + sums[l]
            if total_sum > max_sum:
                max_sum = total_sum
                res = [j, i, l]

        return res
