from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not nums or k <= 0 or 3*k > n:
            return []

        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        left = [0] * n
        bestStart = 0
        for i in range(k, n - 2 * k + 1):
            if sums[i] - sums[i - k] > sums[bestStart] - sums[bestStart - k]:
                bestStart = i - k
            left[i] = bestStart

        right = [0] * n
        bestEnd = n - k
        for i in range(n - k, 2 * k - 1, -1):
            if sums[i + k] - sums[i] >= sums[bestEnd + k] - sums[bestEnd]:
                bestEnd = i
            right[i] = bestEnd

        maxSum = 0
        res = [0, 0, 0]
        for i in range(k, n - 2 * k + 1):
            l, r = left[i], right[i]
            total = (sums[l + k] - sums[l]) + (sums[i + k] - sums[i]) + (sums[r + k] - sums[r])
            if total > maxSum:
                maxSum = total
                res = [l, i, r]

        return res
