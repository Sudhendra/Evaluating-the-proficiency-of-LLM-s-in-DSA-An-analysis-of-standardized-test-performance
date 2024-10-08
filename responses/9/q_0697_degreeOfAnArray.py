from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        left, right, degree = {}, {}, 0
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
            degree = max(degree, count[num])
        
        min_length = len(nums)
        for num in count:
            if count[num] == degree:
                min_length = min(min_length, right[num] - left[num] + 1)

        return min_length
