from bisect import bisect_right

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort_count(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2
            left, count_left = merge_sort_count(nums[:mid])
            right, count_right = merge_sort_count(nums[mid:])
            
            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
                
            return sorted(left + right), count + count_left + count_right

        _, count = merge_sort_count(nums)
        return count