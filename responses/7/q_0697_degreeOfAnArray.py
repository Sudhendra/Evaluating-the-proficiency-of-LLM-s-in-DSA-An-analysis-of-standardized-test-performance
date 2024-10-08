from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occurrence = {}
        degree = 0
        min_length = float('inf')

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            count[num] += 1
            if count[num] > degree:
                degree = count[num]

        for num, freq in count.items():
            if freq == degree:
                min_length = min(min_length, first_occurrence[num])

        for num in reversed(nums):
            if count[num] == degree:
                min_length = min(min_length, len(nums) - first_occurrence[num])

        return min_length

# Test cases
solution = Solution()
print(solution.findShortestSubArray([1,2,2,3,1]))  # Output: 2
print(solution.findShortestSubArray([1,2,2,3,1,4,2]))  # Output: 6
