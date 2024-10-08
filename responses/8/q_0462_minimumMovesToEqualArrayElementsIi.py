class Solution:
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(num - median) for num in nums)

# Example usage:
solution = Solution()
print(solution.minMoves2([1, 2, 3]))  # Output: 2
print(solution.minMoves2([1, 10, 2, 9]))  # Output: 16
