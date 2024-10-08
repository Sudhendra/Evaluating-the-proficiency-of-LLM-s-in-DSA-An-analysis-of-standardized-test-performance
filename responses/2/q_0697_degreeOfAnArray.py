from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occurrence = {}
        degree = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            count[num] += 1
            if count[num] > degree:
                degree = count[num]

        for num, c in count.items():
            if c == degree:
                min_length = min(min_length, first_occurrence[num] + nums.count(num) - first_occurrence[num])

        return min_length
