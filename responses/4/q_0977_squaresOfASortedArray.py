class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        idx = n - 1

        while idx >= 0:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[idx] = left_sq
                left += 1
            else:
                result[idx] = right_sq
                right -= 1

            idx -= 1

        return result
