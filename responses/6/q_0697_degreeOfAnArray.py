from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        first_occurrence = {}  # Store the first occurrence index of each number
        max_count = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            counts[num] += 1
            if counts[num] > max_count:
                max_count = counts[num]
                min_length = i - first_occurrence[num] + 1
            elif counts[num] == max_count:
                min_length = min(min_length, i - first_occurrence[num] + 1)
        
        return min_length
