from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_and_count(left: List[int], right: List[int]) -> (List[int], int):
            merged = []
            count = 0
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    count += len(left) - i
            merged.extend(left[i:] if i < len(left) else right[j:])
            return merged, count
        
        def merge_sort_and_count(nums: List[int]) -> (List[int], int):
            if len(nums) <= 1:
                return nums, 0
            mid = len(nums) // 2
            left, left_count = merge_sort_and_count(nums[:mid])
            right, right_count = merge_sort_and_count(nums[mid:])
            merged, merge_count = merge_and_count(left, right)
            return merged, left_count + right_count + merge_count

        _, count = merge_sort_and_count(nums)
        return count

# Test cases
solution = Solution()
assert solution.reversePairs([1, 3, 2, 3, 1]) == 2
assert solution.reversePairs([2, 4, 3, 5, 1]) == 3
