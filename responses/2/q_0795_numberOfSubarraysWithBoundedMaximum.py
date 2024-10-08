class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays_with_max_less_or_equal(target):
            count, result = 0, 0
            
            for num in nums:
                count = count + 1 if num <= target else 0
                result += count
            
            return result
        
        return count_subarrays_with_max_less_or_equal(right) - count_subarrays_with_max_less_or_equal(left - 1)
