from collections import defaultdict

class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        first_occurrence = {}
        degree = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            freq[num] += 1
            degree = max(degree, freq[num])

        for num, f in freq.items():
            if f == degree:
                min_length = min(min_length, first_occurrence[num]+1 + nums[::-1].index(num))

        return min_length
