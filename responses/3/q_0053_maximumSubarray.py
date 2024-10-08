class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

    def maxSubArray_dc(self, nums: List[int]) -> int:
        def helper(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_sum = helper(nums, left, mid)
            right_sum = helper(nums, mid+1, right)

            left_max = float('-inf')
            current_sum = 0
            for i in range(mid, left-1, -1):
                current_sum += nums[i]
                left_max = max(left_max, current_sum)

            right_max = float('-inf')
            current_sum = 0
            for i in range(mid+1, right+1):
                current_sum += nums[i]
                right_max = max(right_max, current_sum)

            return max(left_sum, right_sum, left_max + right_max)

        return helper(nums, 0, len(nums)-1)