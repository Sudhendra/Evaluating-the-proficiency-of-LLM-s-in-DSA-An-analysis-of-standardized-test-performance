from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_to_count = defaultdict(int)
        num_to_first_idx = {}
        degree = 0
        min_length = float('inf')

        for i, num in enumerate(nums):
            if num not in num_to_first_idx:
                num_to_first_idx[num] = i
            num_to_count[num] += 1
            degree = max(degree, num_to_count[num])

        for num, count in num_to_count.items():
            if count == degree:
                min_length = min(min_length, i - num_to_first_idx[num] + 1)

        return min_length
