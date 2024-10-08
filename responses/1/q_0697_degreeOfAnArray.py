from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        element_count = defaultdict(int)
        first_occurrence = {}
        shortest_subarray_length = len(nums)
        
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            element_count[num] += 1
            if element_count[num] > degree:
                degree = element_count[num]
        
        for num, count in element_count.items():
            if count == degree:
                shortest_subarray_length = min(shortest_subarray_length, i - first_occurrence[num] + 1)
        
        return shortest_subarray_length