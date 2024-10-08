class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        def max_sum(prefix_sum, start, end):
            max_sum = 0
            for i in range(start, end):
                max_sum = max(max_sum, prefix_sum[i+secondLen] - prefix_sum[i])
            return max_sum

        result = 0
        for i in range(1, n):
            prefix_sum[i] = max(prefix_sum[i], prefix_sum[i-1])

        for i in range(firstLen - 1, n):
            result = max(result, prefix_sum[i] + max_sum(prefix_sum, i, n))

        for i in range(secondLen - 1, n):
            result = max(result, prefix_sum[i] + max_sum(prefix_sum, i, n))

        return result