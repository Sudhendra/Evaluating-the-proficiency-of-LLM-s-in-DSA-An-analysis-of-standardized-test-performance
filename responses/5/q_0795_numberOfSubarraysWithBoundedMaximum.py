class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarraysWithMaxLessOrEqual(val):
            count = 0
            curr_count = 0

            for num in nums:
                if num <= val:
                    curr_count += 1
                    count += curr_count
                else:
                    curr_count = 0

            return count
        
        return countSubarraysWithMaxLessOrEqual(right) - countSubarraysWithMaxLessOrEqual(left - 1)