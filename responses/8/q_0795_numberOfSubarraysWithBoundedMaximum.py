class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def count_subarrays(arr):
            count, current = 0, 0
            for num in arr:
                current = current + 1 if left <= num <= right else 0
                count += current
            return count
        
        return count_subarrays(nums) - count_subarrays([num-1 for num in nums])
