class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays_bound(nums: List[int], bound: int) -> int:
            count = 0
            curr_count = 0

            for num in nums:
                if num <= bound:
                    curr_count += 1
                    count += curr_count
                else:
                    curr_count = 0

            return count

        return count_subarrays_bound(nums, right) - count_subarrays_bound(nums, left - 1)