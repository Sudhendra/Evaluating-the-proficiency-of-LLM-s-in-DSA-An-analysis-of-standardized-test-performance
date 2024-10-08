class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubArrayDivideConquer(self, nums: List[int]) -> int:
        def divide_conquer(left, right):
            if left == right:
                return nums[left]

            mid = left + (right - left) // 2

            left_max = divide_conquer(left, mid)
            right_max = divide_conquer(mid + 1, right)

            left_sum = nums[mid]
            current_sum = nums[mid]
            for i in range(mid - 1, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)

            right_sum = nums[mid + 1]
            current_sum = nums[mid + 1]
            for i in range(mid + 2, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)

            return max(left_max, right_max, left_sum + right_sum)

        return divide_conquer(0, len(nums) - 1)