from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_idx = 0
        while neg_idx < len(nums) and nums[neg_idx] < 0:
            neg_idx += 1

        pos_idx = neg_idx
        neg_idx -= 1

        result = []
        while neg_idx >= 0 and pos_idx < len(nums):
            if nums[neg_idx] ** 2 < nums[pos_idx] ** 2:
                result.append(nums[neg_idx] ** 2)
                neg_idx -= 1
            else:
                result.append(nums[pos_idx] ** 2)
                pos_idx += 1

        while neg_idx >= 0:
            result.append(nums[neg_idx] ** 2)
            neg_idx -= 1

        while pos_idx < len(nums):
            result.append(nums[pos_idx] ** 2)
            pos_idx += 1

        return result
