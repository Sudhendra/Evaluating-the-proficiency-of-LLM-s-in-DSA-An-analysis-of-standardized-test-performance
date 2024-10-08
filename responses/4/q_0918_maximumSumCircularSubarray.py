class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = max_sum = min_sum = current_max = current_min = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

            total_sum += num

        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum
