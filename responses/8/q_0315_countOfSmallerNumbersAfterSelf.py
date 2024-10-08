from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        sorted_nums = []

        for i in range(n - 1, -1, -1):
            left, right = 0, len(sorted_nums)
            while left < right:
                mid = left + (right - left) // 2
                if sorted_nums[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            result[i] = left
            sorted_nums.insert(left, nums[i])
        
        return result

# Test cases
solution = Solution()

# Test case 1
print(solution.countSmaller([5, 2, 6, 1]))  # Output: [2, 1, 1, 0]

# Test case 2
print(solution.countSmaller([-1]))  # Output: [0]

# Test case 3
print(solution.countSmaller([-1, -1]))  # Output: [0, 0]
