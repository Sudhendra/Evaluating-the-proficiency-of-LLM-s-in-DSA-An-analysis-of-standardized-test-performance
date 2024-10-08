class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_len = float('inf')
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

    def minSubArrayLenBinarySearch(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        min_len = float('inf')

        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] >= target:
                left = bisect_left(prefix_sum, prefix_sum[i] - target, 0, i)
                min_len = min(min_len, i - left + 1)

        return min_len if min_len != float('inf') else 0